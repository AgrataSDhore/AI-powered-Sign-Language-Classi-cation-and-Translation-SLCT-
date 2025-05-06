# prediction.py

import os
import numpy as np
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.models import load_model # type: ignore
import pickle

# Load the saved models
model_paths = ["Models/Dataset 1_model.h5", "Models/Dataset 2_model.h5", "Models/Dataset 3_model.h5"]
loaded_models = [load_model(path) for path in model_paths]

# Load the class labels for each model
class_label_maps = []
for model_path in model_paths:
    label_map_path = model_path.replace("_model.h5", "_label_map.pkl")
    with open(label_map_path, 'rb') as label_map_file:
        class_label_map = pickle.load(label_map_file)
    class_label_maps.append(class_label_map)

# Function to preprocess a single image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(64, 64))  # Assuming input shape is (64, 64, 3)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize
    return img_array

# Function to predict sign
def predict_sign(image_file):
    # Save the uploaded image to a temporary location
    temp_image_path = 'temp_image.jpg'
    image_file.save(temp_image_path)

    # Preprocess the image
    preprocessed_image = preprocess_image(temp_image_path)

    # Make predictions with each model
    all_predictions = []
    for model in loaded_models:
        predictions = model.predict(preprocessed_image.reshape(1, 64, 64, 3))
        all_predictions.append(predictions)

    # Get the maximum number of classes among all models
    max_classes = max(predictions.shape[1] for predictions in all_predictions)

    # Pad prediction arrays with zeros to ensure they have the same length
    padded_predictions = []
    for predictions in all_predictions:
        padded_predictions.append(np.pad(predictions, ((0, 0), (0, max_classes - predictions.shape[1])), mode='constant'))

    # Stack the padded predictions along a new axis
    stacked_predictions = np.stack(padded_predictions, axis=0)

    # Aggregate predictions
    aggregate_predictions = np.mean(stacked_predictions, axis=0)  # Assuming averaging of probabilities

    predicted_class_index = np.argmax(aggregate_predictions)

    # Retrieve the predicted class label for the current model
    #predicted_class_label = class_label_maps[0][predicted_class_index] if predicted_class_index < len(class_label_maps[0]) else "Unknown"

    # Initialize variables to store the maximum confidence and the corresponding predicted class label
    max_confidence = 0
    predicted_class_label = None
    # Iterate over each class label map and its corresponding model
    for class_label_map, predictions in zip(class_label_maps, all_predictions):
        # Retrieve the predicted class label for the current model
        if predicted_class_index < len(class_label_map):
            current_predicted_class_label = class_label_map[predicted_class_index]
        else:
            current_predicted_class_label = "Unknown"  
        # Calculate the confidence score for the current model
        current_confidence = predictions[0][predicted_class_index]
        # Print the predicted class label and confidence score for the current model
        print("Predicted class label:", current_predicted_class_label, " & ", "Confidence score:", current_confidence)
        # Update the maximum confidence and corresponding predicted class label if needed
        if current_confidence > max_confidence:
            max_confidence = current_confidence
            predicted_class_label = current_predicted_class_label
    
    # Delete the temporary image file
    os.remove(temp_image_path)

    return predicted_class_label
