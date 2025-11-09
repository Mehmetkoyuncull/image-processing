import cv2

image = cv2.imread('arda.jpg')

if image is None:
    exit()

negative_image = 255 - image

cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
