from flask import Flask, request, jsonify
import os
from datetime import datetime
import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_human(image):
    # Load the pre-trained Haar Cascade classifiers for human detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

    # Convert the image to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces and upper bodies in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    upper_bodies = upperbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If faces or upper bodies are detected, return True (human detected)
    if len(faces) > 0 or len(upper_bodies) > 0:
        return True
    else:
        return False

def send_email(image):
    # Configure email parameters
    sender_email = "dhruvvisariya666@gmail.com"
    receiver_email = "dhruvvisariya1234@gmail.com"
    password = "jbmh jgjw rtfn ggex"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Human Detected'

    # Email body
    body = 'A human has been detected in the uploaded image.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image
    _, img_encoded = cv2.imencode('.jpg', image)
    img_as_bytes = img_encoded.tobytes()
    img_attachment = MIMEImage(img_as_bytes)
    img_attachment.add_header('Content-Disposition', 'attachment', filename="detected_image.jpg")
    msg.attach(img_attachment)

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image/jpeg' not in request.headers.get('Content-Type'):
        return jsonify({'error': 'Unsupported media type'})

    image_data = request.get_data()
    if not image_data:
        return jsonify({'error': 'No image data received'})

    now = datetime.now()
    timestamp = now.strftime("%Y.%m.%d_%H:%M:%S_")
    filename = timestamp + 'esp32_image.jpg'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(filepath, 'wb') as f:
        f.write(image_data)

    # Load the image for processing
    image = cv2.imread(filepath)

    # Detect if there is a human in the image
    if detect_human(image):
        # Send email if human detected
        send_email(image)
        return jsonify({'message': 'Human detected. Email sent.'})
    else:
        return jsonify({'message': 'No human detected.'})

if __name__ == '__main__':
    app.run(debug=False)
