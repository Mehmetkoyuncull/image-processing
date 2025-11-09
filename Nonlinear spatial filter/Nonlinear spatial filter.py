import cv2
import matplotlib.pyplot as plt

ayi_image = cv2.imread("AA.jpg.")
if ayi_image is None:
    exit()

ayi_image_rgb = cv2.cvtColor(ayi_image, cv2.COLOR_BGR2RGB)

median_filtered_image = cv2.medianBlur(ayi_image_rgb, 5)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(ayi_image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(median_filtered_image)
plt.axis("off")

plt.tight_layout()
plt.show()
