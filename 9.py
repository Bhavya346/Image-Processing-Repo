import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Flatten image
flat = img.flatten()

# 🔹 Run Length Encoding (RLE)
rle = []
prev = flat[0]
count = 1

for pixel in flat[1:]:
    if pixel == prev:
        count += 1
    else:
        rle.append((prev, count))
        prev = pixel
        count = 1

# Append last run
rle.append((prev, count))

# Output sizes
print("Original size:", len(flat))
print("RLE size:", len(rle))