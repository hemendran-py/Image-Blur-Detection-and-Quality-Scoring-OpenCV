# Image Blur Detection and Quality Scoring

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A complete web application for detecting image blur using Laplacian variance with OpenCV. Features a Flask REST API backend and a responsive HTML/JavaScript frontend for easy image quality assessment.
<div style="display: flex; gap: 20px; justify-content: center;">
  <img src="https://github.com/user-attachments/assets/549a2721-2434-4faf-9ab2-f3ecaf66edde" width="400">
  <img src="https://github.com/user-attachments/assets/54b59257-d096-4e7c-bd79-25bbfcac6bca" width="400">
</div>
## 🚀 Features

- **Blur Detection**: Uses Laplacian variance algorithm for accurate blur measurement
- **REST API**: Clean Flask API endpoint for image processing
- **Web Interface**: Simple, responsive frontend for uploading and analyzing images
- **Real-time Preview**: Instant image preview before processing
- **Error Handling**: Comprehensive error handling for invalid inputs
- **CORS Support**: Cross-origin resource sharing enabled for web integration

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd image-blur-detection
   ```

2. **Install backend dependencies:**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "import cv2, flask; print('All dependencies installed successfully')"
   ```

## 🎯 Usage

### Running the Application

1. **Start the Flask backend:**

   ```bash
   cd backend
   python app.py
   ```

   The server will start on `http://localhost:5000`

2. **Open the frontend:**
   - Open `frontend/index.html` in your web browser
   - Or serve it through a local web server for better functionality

3. **Upload and analyze:**
   - Select an image file (PNG, JPG, JPEG, GIF)
   - Click "Upload and Analyze"
   - View the blur score and classification

### Example Usage

```bash
# Start the backend
python backend/app.py

# In another terminal, test the API
curl -X POST -F "image=@sharp_image.jpg" http://localhost:5000/score
```

## 📚 API Documentation

### POST /score

Upload an image and receive blur detection results.

#### Request

- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Body Parameters:**
  - `image` (file): Image file to analyze

#### Response

**Success (200):**

```json
{
  "score": 1234.56,
  "category": "Medium Blur"
}
```

**Error (400/500):**

```json
{
  "error": "Error message description"
}
```

#### Response Fields

- `score` (float): Laplacian variance value (higher = sharper)
- `category` (string): Classification based on score thresholds

#### Classification Thresholds

- **Sharp**: score > 1500
- **Medium Blur**: 500 ≤ score ≤ 1500
- **High Blur**: score < 500

#### Example with curl

```bash
curl -X POST \
  -F "image=@path/to/your/image.jpg" \
  http://localhost:5000/score
```

#### Example with Python

```python
import requests

url = 'http://localhost:5000/score'
files = {'image': open('image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

## 🔍 How It Works

### Laplacian Variance Method

The blur detection algorithm uses the Laplacian operator to measure image sharpness:

1. **Convert to Grayscale**: Transform the image to grayscale for processing
2. **Apply Laplacian**: Compute the Laplacian of the image using OpenCV
3. **Calculate Variance**: Measure the variance of the Laplacian result
4. **Classify**: Compare variance against predefined thresholds

### Mathematical Background

The Laplacian operator highlights regions of rapid intensity change. For a grayscale image \( I \), the Laplacian \( \nabla^2 I \) is computed, and its variance \( \sigma^2 \) serves as a blur metric:

\[ \sigma^2 = \frac{1}{N} \sum ( \nabla^2 I - \mu )^2 \]

Where:

- \( N \) is the number of pixels
- \( \mu \) is the mean Laplacian value

Higher variance indicates sharper images with more high-frequency content.

## 📁 Project Structure

```
image-blur-detection/
├── backend/
│   ├── app.py                 # Flask application and API endpoints
│   ├── utils/
│   │   └── blur_detector.py   # Core blur detection logic
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html             # Main web interface
│   ├── style.css              # CSS styling
│   └── script.js              # Frontend JavaScript logic
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

## 📦 Dependencies

### Backend

- **Flask** (3.1.2): Web framework for API
- **OpenCV** (4.13.0): Computer vision library for image processing
- **NumPy** (1.24.3): Numerical computing
- **Flask-CORS** (4.0.0): Cross-origin resource sharing

### Frontend

- **Vanilla JavaScript**: No external libraries required
- **HTML5**: Modern web standards
- **CSS3**: Responsive styling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add docstrings to all functions
- Write tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenCV community for the computer vision library
- Flask community for the web framework
- Contributors and users of this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include error messages, Python version, and steps to reproduce

---

**Note:** This project is for educational and demonstration purposes. For production use, consider additional security measures, input validation, and performance optimizations.
