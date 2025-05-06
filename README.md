# AI-powered-Sign-Language-Classi-cation-and-Translation-SLCT-
AI-powered Sign Language Classiﬁcation and Translation (SLCT) using TensorFlow Keras Library

# Sign Recognition Web Application

This project is a Flask-based web application that predicts signs from uploaded images using deep learning models.  
Models are pre-trained using CNNs (TensorFlow/Keras) and saved as `.h5` files for deployment. The `.pkl` files store label encoders to convert model output into readable labels.

### Features
- Multi-model prediction pipeline (three datasets supported)
- Image preprocessing (resize, normalize)
- Real-time prediction through web interface
- MySQL backend for user session/data management
- Modular and scalable architecture

### Tech Stack
- Python, Flask, TensorFlow, Keras
- MySQL
- HTML/CSS (for frontend)
