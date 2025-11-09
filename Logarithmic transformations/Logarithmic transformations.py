import cv2
import numpy as np

image = cv2.imread('meyve.jpg')

if image is None:
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = np.float32(gray_image)

c = 255 / np.log(1 + np.max(gray_image))
log_image = c * np.log(1 + gray_image)

log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow('Original Image', image)
cv2.imshow('Logarithmic Transformation', log_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
