import cv2
import numpy as np

image = cv2.imread('beyin.jpg')

if image is None:
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

lower_bound = 100
upper_bound = 200

sliced_image = np.zeros_like(gray_image)
sliced_image[(gray_image >= lower_bound) & (gray_image <= upper_bound)] = 255

cv2.imshow('Original Image', image)
cv2.imshow('Intensity-Level Slicing', sliced_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
