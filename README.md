# 👁️ Real-Time Face and Eye Detection System

A real-time Computer Vision application built using **Python and OpenCV** that detects human faces and eyes through a live webcam feed using Haar Cascade Classifiers.

The system processes video frames continuously, identifies facial regions, detects eyes within those regions, and highlights the detected objects using bounding boxes.

## 🚀 Project Overview

Face and eye detection is a fundamental application of Computer Vision used in facial analysis, surveillance systems, human-computer interaction, and camera-based monitoring.

This project demonstrates how traditional Computer Vision techniques can be used to detect facial features from real-time video streams.

### ✨ Key Features

- **Real-Time Face Detection:** Detects human faces through a webcam.
- **Eye Detection:** Identifies eyes within detected facial regions.
- **Haar Cascade Classification:** Uses pre-trained Haar Cascade XML classifiers.
- **Live Video Processing:** Processes webcam frames continuously.
- **Visual Detection:** Draws bounding boxes around detected faces and eyes.
- **Image Preprocessing:** Converts video frames into grayscale for detection.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Computer Vision and image processing |
| Haar Cascade | Face and eye detection |
| NumPy | Numerical and array operations |
| Webcam | Real-time video input |

## ⚙️ How It Works

The application follows these processing steps:

1. **Video Capture:** Captures live video using the computer's webcam.
2. **Grayscale Conversion:** Converts each video frame from BGR to grayscale.
3. **Face Detection:** Uses the Haar Cascade face classifier to identify faces.
4. **Eye Detection:** Searches for eyes within the detected face regions.
5. **Bounding Boxes:** Draws rectangles around detected faces and eyes.
6. **Live Display:** Displays the processed video stream in real time.

## 📂 Project Structure

```text
Face-Eye-Detection/
│
├── models/
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_eye.xml
│
├── face_eye_detection.py
├── requirements.txt
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Face-Eye-Detection
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python face_eye_detection.py
```

Make sure your webcam is connected and accessible.

Press **Q** to close the application.

## 📦 Dependencies

Add the following to `requirements.txt`:

```text
opencv-python
numpy
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding fundamental Computer Vision concepts.
- Working with OpenCV for real-time image processing.
- Implementing Haar Cascade Classifiers.
- Performing grayscale conversion and image preprocessing.
- Detecting facial features from live webcam streams.
- Working with video capture and frame processing.

## 🔮 Future Enhancements

- Implement facial recognition to distinguish individuals.
- Explore more advanced face detection models such as SSD or YOLO.
- Integrate facial landmark detection.
- Develop a real-time driver drowsiness monitoring system.
- Improve detection accuracy under different lighting conditions.

## 👨‍💻 Author

**Reyhan**

B.E. Computer Science and Engineering

- GitHub: https://github.com/Reyhan07-afi

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python and OpenCV | Exploring the fundamentals of Computer Vision.**
