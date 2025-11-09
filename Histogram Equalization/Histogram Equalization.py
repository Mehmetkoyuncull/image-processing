import cv2
import numpy as np

image = cv2.imread('tekne.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (800, 600))
equalized_image = cv2.equalizeHist(image)

cv2.imshow('Original Image', image)
cv2.imshow('Histogram Equalized Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
