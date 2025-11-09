import cv2
import matplotlib.pyplot as plt

image = cv2.imread('tsun.jpg', cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for proper color display

median_filtered_image = cv2.medianBlur(image, 5)  # Kernel size is 5x5
median_rgb = cv2.cvtColor(median_filtered_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Median Filtered Image")
plt.imshow(median_rgb)
plt.axis('off')

plt.show()
