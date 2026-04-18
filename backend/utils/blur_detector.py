import cv2
import numpy as np

def detect_blur(image_path):
    """
    Detect blur in an image using Laplacian variance.

    Args:
        image_path (str): Path to the image file.

    Returns:
        float: The variance of the Laplacian, indicating blur level.

    Raises:
        ValueError: If the image cannot be loaded.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Invalid image file or unable to load image.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute Laplacian variance
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    variance = laplacian.var()
    
    return variance