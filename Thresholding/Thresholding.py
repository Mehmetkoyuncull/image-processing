import cv2

image = cv2.imread('zambak.jpg')

if image is None:
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply simple binary thresholding
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
