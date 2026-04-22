import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('445566.jpg')

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range (RED example)
lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower, upper)

# Apply mask
segmented = cv2.bitwise_and(img, img, mask=mask)

# Show results
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
plt.title('Segmented')
plt.axis('off')

plt.show()