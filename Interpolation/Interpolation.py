import cv2
import numpy as np


image = cv2.imread('atlet.jpg')

if image is None:
    print("Error: Image not found.")
    exit()

nearest_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_NEAREST)

bilinear_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)

bicubic_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_CUBIC)

lanczos_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Original Image', image)
cv2.imshow('Nearest Neighbor', nearest_image)
cv2.imshow('Bilinear Interpolation', bilinear_image)
cv2.imshow('Bicubic Interpolation', bicubic_image)
cv2.imshow('Lanczos Interpolation', lanczos_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
