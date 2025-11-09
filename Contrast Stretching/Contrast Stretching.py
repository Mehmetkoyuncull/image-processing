import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('erkan.jpg', cv2.IMREAD_GRAYSCALE)

def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

stretched_image = contrast_stretching(image)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contrast Stretched Image")
plt.imshow(stretched_image, cmap='gray')
plt.axis('off')

plt.show()

cv2.imwrite('contrast_stretched_erkan.jpg', stretched_image)
