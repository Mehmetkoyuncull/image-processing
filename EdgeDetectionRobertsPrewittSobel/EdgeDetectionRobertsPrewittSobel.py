import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('konya.jpg', cv2.IMREAD_GRAYSCALE)

roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
roberts_edge_x = cv2.filter2D(image, -1, roberts_x)
roberts_edge_y = cv2.filter2D(image, -1, roberts_y)
roberts_edge = cv2.magnitude(roberts_edge_x.astype(np.float32), roberts_edge_y.astype(np.float32))

prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
prewitt_edge_x = cv2.filter2D(image, -1, prewitt_x)
prewitt_edge_y = cv2.filter2D(image, -1, prewitt_y)
prewitt_edge = cv2.magnitude(prewitt_edge_x.astype(np.float32), prewitt_edge_y.astype(np.float32))

sobel_edge_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_edge_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edge = cv2.magnitude(sobel_edge_x, sobel_edge_y)

plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Roberts Edge Detection")
plt.imshow(roberts_edge, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Prewitt Edge Detection")
plt.imshow(prewitt_edge, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Sobel Edge Detection")
plt.imshow(sobel_edge, cmap='gray')
plt.axis('off')

plt.show()

cv2.imwrite('roberts_konya.jpg', roberts_edge.astype(np.uint8))
cv2.imwrite('prewitt_konya.jpg', prewitt_edge.astype(np.uint8))
cv2.imwrite('sobel_konya.jpg', sobel_edge.astype(np.uint8))
