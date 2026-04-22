import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Convert to binary image
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Morphological operations
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)

# Display results
cv2.imshow('Binary', binary)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()