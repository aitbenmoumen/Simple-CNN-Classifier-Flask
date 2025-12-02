# 🍎 Fruit Classifier - CNN Flask Application

A deep learning web application that classifies fruit images using a Convolutional Neural Network (CNN) model built with TensorFlow/Keras and deployed with Flask.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## 🎯 Overview

This project implements a CNN-based image classification system that can identify three types of fruits: **apples**, **bananas**, and **oranges**. The model is deployed as a web application using Flask, providing an intuitive interface for users to upload images and receive predictions.

## ✨ Features

- 🖼️ **Image Upload**: Support for multiple image formats (PNG, JPG, JPEG, GIF, BMP)
- 🤖 **CNN Classification**: Deep learning model for accurate fruit recognition
- 📊 **Confidence Scores**: Detailed prediction probabilities for all classes
- 💻 **Responsive UI**: Modern, user-friendly interface
- 🚀 **Real-time Predictions**: Fast inference with instant results
- 🔒 **Secure File Handling**: Validated file uploads with size restrictions
- ❤️ **Health Check**: API endpoint for monitoring service status

## 🛠️ Technologies

### Backend
- **Python 3.x**
- **Flask 3.1.2** - Web framework
- **TensorFlow 2.20.0** - Deep learning framework
- **Keras 3.12.0** - Neural network API
- **NumPy 2.2.6** - Numerical computing
- **Pillow 12.0.0** - Image processing

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

## 📁 Project Structure

```
Flask-app/
│
├── app.py                          # Main Flask application
├── req.txt                         # Python dependencies
├── readme                          # Project documentation
│
├── models/
│   └── fruit_classifier_modelCNN.h5    # Trained CNN model
│
├── utils/
│   ├── model_utils.py              # Model inference utilities
│   └── __pycache__/
│
├── static/
│   ├── css/
│   │   └── style.css               # Application styles
│   ├── js/
│   │   └── script.js               # Frontend logic
│   └── uploads/                    # Uploaded images directory
│
└── templates/
    └── index.html                  # Main web interface
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/aitbenmoumen/Simple-CNN-Classifier-Flask.git
   cd Flask-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r req.txt
   ```

4. **Verify model file**
   Ensure `fruit_classifier_modelCNN.h5` exists in the `models/` directory.

## 💡 Usage

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Classify fruits**
   - Click "Browse" to select an image
   - Preview the uploaded image
   - Click "🔍 Classify Fruit"
   - View the prediction results with confidence scores

## 🧠 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Input Size**: 32x32 pixels (RGB)
- **Classes**: 3 (Apple, Banana, Orange)
- **Framework**: TensorFlow/Keras

### Classes
1. 🍎 Apple
2. 🍌 Banana
3. 🍊 Orange

### Preprocessing
- Images are resized to 32x32 pixels
- Converted to RGB format
- Pixel values normalized (if enabled)

## 🔌 API Endpoints

### `GET /`
Returns the main web interface.

### `POST /predict`
Accepts image uploads and returns classification results.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `file` (image file)

**Response:**
```json
{
  "predicted_class": "apple",
  "confidence": 95.67,
  "all_predictions": {
    "apple": 95.67,
    "banana": 3.21,
    "orange": 1.12
  },
  "image_url": "/static/uploads/image.jpg"
}
```

### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## 📸 Screenshots

### Main Interface
Upload and classify fruit images with an intuitive interface.

### Prediction Results
View detailed confidence scores for all fruit classes.

## 🔧 Configuration

### File Upload Settings
- **Max File Size**: 16 MB
- **Allowed Extensions**: PNG, JPG, JPEG, GIF, BMP
- **Upload Directory**: `static/uploads/`

### Server Settings
- **Host**: 127.0.0.1
- **Port**: 5000
- **Debug Mode**: Enabled (development)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Ait Ben Moumen**
- GitHub: [@aitbenmoumen](https://github.com/aitbenmoumen)


**Note**: This is an educational project for demonstrating CNN-based image classification with Flask deployment.
