from scipy.signal import wiener
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('445566.jpg', 0)

if img is None:
    print("Error: Image not found")
    exit()

noise = 20 * np.sin(np.linspace(0, 50, img.shape[1]))
noise = np.tile(noise, (img.shape[0], 1))

noisy = img + noise
noisy = np.clip(noisy, 0, 255)

wiener_img = wiener(noisy.astype(float))

plt.imshow(wiener_img, cmap='gray')
plt.title('Wiener Filtered Image')
plt.axis('off')
plt.show()