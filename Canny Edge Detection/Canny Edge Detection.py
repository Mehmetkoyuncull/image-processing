import cv2
import matplotlib.pyplot as plt

image = cv2.imread('max.jpg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5, 5), 1.0)
edges = cv2.Canny(blurred, 100, 200)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Canny Edge Detection")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()

cv2.imwrite('canny_max.jpg', edges)
