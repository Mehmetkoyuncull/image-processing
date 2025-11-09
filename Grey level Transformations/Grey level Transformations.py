import cv2
import numpy as np

image = cv2.imread('dag.jpg')

if image is None:
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

negative_image = 255 - gray_image

c = 255 / np.log(1 + np.max(gray_image))
log_image = c * np.log(1 + gray_image)
log_image = np.array(log_image, dtype=np.uint8)

gamma = 1.5
c = 255 / np.max(gray_image) ** gamma
power_law_image = c * (gray_image ** gamma)
power_law_image = np.array(power_law_image, dtype=np.uint8)

cv2.imshow('Original Image', image)
cv2.imshow('Negative Transformation', negative_image)
cv2.imshow('Log Transformation', log_image)
cv2.imshow('Power-Law Transformation', power_law_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
