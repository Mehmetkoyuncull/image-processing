import cv2
import numpy as np

image = cv2.imread('aslan.jpg')

if image is None:
    exit()

image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(gray_image)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(gray_image)

gamma = 1.5
gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype='uint8')

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, kernel)

gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Histogram Equalization', equalized_image)
cv2.imshow('CLAHE', clahe_image)
cv2.imshow('Gamma Correction', gamma_corrected)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('Gaussian Blur', gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
