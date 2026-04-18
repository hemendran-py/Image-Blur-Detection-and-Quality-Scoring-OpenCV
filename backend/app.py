from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.blur_detector import detect_blur
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/score', methods=['POST'])
def score():
    """
    API endpoint to score image blur.

    Expects a POST request with an 'image' file.

    Returns JSON with score and category.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only images are allowed.'}), 400
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    try:
        score = detect_blur(filepath)
        if score > 1500:
            category = 'Sharp'
        elif 500 <= score <= 1500:
            category = 'Medium Blur'
        else:
            category = 'High Blur'
        
        return jsonify({'score': score, 'category': category})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    finally:
        # Clean up the uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)