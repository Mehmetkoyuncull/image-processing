import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('era.jpg', cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

num_labels, labels = cv2.connectedComponents(binary_image)

colored_labels = cv2.applyColorMap(np.uint8(labels * 255 / num_labels), cv2.COLORMAP_JET)

plt.subplot(121), plt.imshow(binary_image, cmap='gray'), plt.title('Binary Image')
plt.subplot(122), plt.imshow(colored_labels), plt.title('Connected Components')
plt.show()

print(f"Total connected components found: {num_labels - 1}")
