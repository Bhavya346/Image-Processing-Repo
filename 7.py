import cv2
import numpy as np

# Read image
img = cv2.imread('445566.jpg')

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Get dimensions
rows, cols = img.shape[:2]

# 🔹 Translation
M_trans = np.float32([[1, 0, 50], [0, 1, 50]])
translated = cv2.warpAffine(img, M_trans, (cols, rows))

# 🔹 Scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

# 🔹 Rotation
M_rot = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M_rot, (cols, rows))

# Show results
cv2.imshow('Translated', translated)
cv2.imshow('Scaled', scaled)
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()