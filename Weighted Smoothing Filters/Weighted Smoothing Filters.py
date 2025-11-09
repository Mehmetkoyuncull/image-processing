import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('yang.jpg', cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
weighted_smoothed_image = cv2.filter2D(image, -1, kernel)
smoothed_rgb = cv2.cvtColor(weighted_smoothed_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Weighted Smoothed Image")
plt.imshow(smoothed_rgb)
plt.axis('off')

plt.show()
