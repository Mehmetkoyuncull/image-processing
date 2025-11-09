import cv2
import matplotlib.pyplot as plt

image = cv2.imread('top.jpg', cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)
enhanced_image = cv2.addWeighted(image, 1.0, laplacian, -1.0, 0)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Laplacian Filtered Image")
plt.imshow(laplacian, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Enhanced Image")
plt.imshow(enhanced_image, cmap='gray')
plt.axis('off')

plt.show()
