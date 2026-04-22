import cv2
from collections import Counter

# Read image
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Count pixel frequencies
freq = Counter(img.flatten())

# Print result
print("Pixel Frequencies:", freq)