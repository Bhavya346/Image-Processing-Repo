import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Apply thresholding
_, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Display result
cv2.imshow('Threshold Segmentation', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()