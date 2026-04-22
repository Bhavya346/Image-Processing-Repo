import cv2

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Apply threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Check if any contour found
if len(contours) == 0:
    print("No contours found")
else:
    print("Number of boundary points:", len(contours[0]))