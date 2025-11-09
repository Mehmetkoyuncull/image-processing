import cv2
import numpy as np
import matplotlib.pyplot as plt

dog_image = cv2.imread("dog.jpg")
if dog_image is None:
    raise FileNotFoundError("The file 'dog.png' was not found. Make sure it's in the same directory as the script.")

dog_image_rgb = cv2.cvtColor(dog_image, cv2.COLOR_BGR2RGB)

kernel_size = (5, 5)  # Size of the kernel (larger values = more blur)
blurred_image = cv2.GaussianBlur(dog_image_rgb, kernel_size, sigmaX=0)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(dog_image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gaussian Blurred Image")
plt.imshow(blurred_image)
plt.axis("off")

plt.tight_layout()
plt.show()
