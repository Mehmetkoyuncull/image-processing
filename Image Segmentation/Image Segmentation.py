import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('tarkan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
segmented = image.copy()
cv2.drawContours(segmented, contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Segmented Image")
plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()

cv2.imwrite('segmented_tarkan.jpg', segmented)
