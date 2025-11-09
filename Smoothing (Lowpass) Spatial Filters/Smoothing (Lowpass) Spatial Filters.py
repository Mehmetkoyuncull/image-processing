import cv2
import matplotlib.pyplot as plt

monkey_image = cv2.imread("monkey.jpg")
if monkey_image is None:
    exit()

monkey_image_rgb = cv2.cvtColor(monkey_image, cv2.COLOR_BGR2RGB)

kernel = (13, 13)
average_filtered_image = cv2.blur(monkey_image_rgb, kernel)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(monkey_image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(average_filtered_image)
plt.axis("off")

plt.tight_layout()
plt.show()