import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded properly
if img is None:
    print("Error: Image not found")
else:
    values, counts = np.unique(img, return_counts=True)
    prob = counts / counts.sum()

    print("Symbol Probabilities:", prob)