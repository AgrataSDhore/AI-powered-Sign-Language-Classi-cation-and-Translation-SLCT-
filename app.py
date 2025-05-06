from flask import Flask, render_template, request, send_from_directory, request,redirect,session,url_for,jsonify # type: ignore
from flask_mysqldb import MySQL # type: ignore
import Admin as adm
from prediction import predict_sign
from PIL import Image
from io import BytesIO

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contacts_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/getsign")
def getsign():
    return render_template("getsign.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route('/static/css/<path:path>')
def serve_css(path):
    return send_from_directory('static/css', path)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    jsonVar = request.json
    name = jsonVar['name'] 
    email = jsonVar['email'] 
    message = jsonVar['message']  
    if not name or not email or not message:
        resp = jsonify({'message' : 'All fields are required!'})
        resp.status_code = 409
        return resp
    else:
        try:
            adm.addContactData(name,email,message)
            resp = jsonify({'message' : 'Form submitted successfully'})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'message' : 'An error occurred'})
            resp.status_code = 400
            return resp
    
@app.route('/predict_sign', methods=['POST'])
def predict_sign_img():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    image_file = request.files['image']
    img = Image.open(BytesIO(image_file.read()))
    predicted_label = predict_sign(img)
    
    return jsonify({'predicted_label': predicted_label})

if __name__ == "__main__":
    app.run(debug=True)