import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('bal.jpg')

median_filtered = cv2.medianBlur(image, 15)

bilateral_filtered = cv2.bilateralFilter(image, 15, 75, 75)

kernel = np.ones((15, 15), np.uint8)
erosion_filtered = cv2.erode(image, kernel, iterations=1)

dilation_filtered = cv2.dilate(image, kernel, iterations=1)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(median_filtered, cv2.COLOR_BGR2RGB))
plt.title("Median Filter")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(bilateral_filtered, cv2.COLOR_BGR2RGB))
plt.title("Bilateral Filter")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(erosion_filtered, cv2.COLOR_BGR2RGB))
plt.title("Erosion Filter")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(dilation_filtered, cv2.COLOR_BGR2RGB))
plt.title("Dilation Filter")
plt.axis('off')

plt.tight_layout()
plt.show()
