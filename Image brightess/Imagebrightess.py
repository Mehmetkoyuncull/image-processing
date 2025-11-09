import cv2
import numpy as np

image = cv2.imread("example.png")
new_image = cv2.resize(image, (400, 600))

cv2.imshow("Original Image", new_image)

brightness_factor = 50
bright_image = cv2.convertScaleAbs(new_image, alpha=1, beta=brightness_factor)

cv2.imshow("Brightened Image", bright_image)

cv2.imwrite("brightened_example.jpg", bright_image)

cv2.waitKey(0)
cv2.destroyAllWindows()