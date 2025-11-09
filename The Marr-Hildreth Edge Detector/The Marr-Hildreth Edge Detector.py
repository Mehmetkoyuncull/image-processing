import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('tol.jpg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5, 5), 1.0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
marr_hildreth = np.uint8(np.absolute(laplacian))

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Marr-Hildreth Edge Detection")
plt.imshow(marr_hildreth, cmap='gray')
plt.axis('off')

plt.show()

cv2.imwrite('marr_hildreth_tol.jpg', marr_hildreth)
