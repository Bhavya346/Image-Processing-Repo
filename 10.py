import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('445566.jpg', 0)

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Apply Canny Edge Detection
edges = cv2.Canny(img, 100, 200)

# Display images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.axis('off')

plt.show()