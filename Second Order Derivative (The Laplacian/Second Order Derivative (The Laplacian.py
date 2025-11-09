import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cev.jpg', cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Laplacian Filter (Second Derivative)")
plt.imshow(laplacian, cmap='gray')
plt.axis('off')

plt.show()
