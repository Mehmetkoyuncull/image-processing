import cv2
import matplotlib.pyplot as plt

horse_image = cv2.imread("horse.jpg")
if horse_image is None:
    exit()

horse_image_rgb = cv2.cvtColor(horse_image, cv2.COLOR_BGR2RGB)

gaussian_filtered_image = cv2.GaussianBlur(horse_image_rgb, (9, 9), 2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(horse_image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered_image)
plt.axis("off")

plt.tight_layout()
plt.show()