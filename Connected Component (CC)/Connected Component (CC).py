import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (for example, as a grayscale image)
image = cv2.imread('adel.jpg', cv2.IMREAD_GRAYSCALE)

# Threshold the image to get a binary image
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Find connected components
num_labels, labels = cv2.connectedComponents(binary_image)

# Create an output image where the connected components will be colored
output_image = cv2.applyColorMap(np.uint8(labels * 255 / num_labels), cv2.COLORMAP_JET)

# Show the images
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.title('Binary Image')
plt.imshow(binary_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Connected Components')
plt.imshow(output_image)
plt.show()

# Optionally, you can save the output image:
cv2.imwrite('connected_components_output.jpg', output_image)
