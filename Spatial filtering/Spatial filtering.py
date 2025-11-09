import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('vazo.jpg.', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found.")
    exit()

gaussian_blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

sobel_edges = cv2.magnitude(sobel_x, sobel_y)
sobel_edges = np.uint8(np.absolute(sobel_edges))

sharpening_kernel = np.array([[0, -1, 0],
                               [-1, 5,-1],
                               [0, -1, 0]])

sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(gaussian_blurred_image, cmap='gray')
plt.title('Gaussian Blurred Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')
plt.axis('off')

plt.show()
