# ESP32 CAM Object Detection and Alert System

This project is phase 2 of the "Object Detection and Identification" series. It enhances the previous project by adding functionality to detect humans in captured images and send email alerts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project involves:
1. Capturing an image using the ESP32 CAM module when an ultrasonic sensor detects an object.
2. Sending the captured image to a Flask backend.
3. Using OpenCV Haarcascade to identify humans in the image.
4. Sending an email alert if a human is detected using the SMTP library in Python.

## Features

- **ESP32 CAM Module**: Captures images upon detecting an object.
- **Ultrasonic Sensor**: Triggers the ESP32 CAM to capture images.
- **Flask Backend**: Receives and processes images.
- **Human Detection**: Uses OpenCV Haarcascade to detect humans in images.
- **Email Alerts**: Sends email alerts if a human is detected.

## Technologies Used

- **ESP32 CAM Module**
- **Ultrasonic Sensor**
- **Flask (Python)**
- **OpenCV**
- **SMTP (Python)**
- **Arduino IDE**

## Setup Instructions

### Hardware Setup

1. **ESP32 CAM Module**: Connect the ESP32 CAM to the ultrasonic sensor.
2. **Ultrasonic Sensor**: Ensure proper wiring between the ESP32 CAM and the ultrasonic sensor.
   
<img width="480" alt="diagram" src="https://github.com/Dhruvvisariya/OD-I-phase-2/assets/98723934/b50da03a-5bca-4210-96af-0aae79b5a049">

### Software Setup

1. **Arduino IDE**: Install the Arduino IDE and necessary libraries for ESP32.
2. **Flask Backend**:
   - Set up a Flask application.
   - Install required Python libraries: `flask`, `opencv-python`, `numpy`, `smtplib`.
3. **ESP32 CAM Code**: Upload the provided code to the ESP32 CAM module via the Arduino IDE. Ensure you include your Flask backend URL and Wi-Fi details.
4. **Human Detection**:
   - Download the Haarcascade XML file for human detection.
   - Integrate it into your Flask backend for image processing.

## Usage

1. Power on the ESP32 CAM module.
2. The ultrasonic sensor will detect objects and trigger the camera to capture images.
3. Captured images will be sent to the Flask backend.
4. The Flask backend will process the image using OpenCV Haarcascade to detect humans.
5. If a human is detected, an email alert will be sent using the SMTP library.

## Future Work

This project is part of the "Object Detection and Identification" series. Future phases will include:
- Enhancing detection algorithms for better accuracy.
- Adding support for multiple objects and alert types.
- Integrating with more advanced notification systems.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request with detailed information on proposed changes.

---

This README provides an overview of the ESP32 CAM Object Detection and Alert System project, including setup instructions and usage guidelines.

