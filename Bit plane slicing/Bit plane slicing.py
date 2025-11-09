import cv2
import numpy as np

image = cv2.imread('cat.png')

if image is None:
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bit_planes = []
for i in range(8):
    bit_plane = (gray_image >> i) & 1
    bit_planes.append(bit_plane * 255)

bit_planes = [np.array(plane, dtype=np.uint8) for plane in bit_planes]

resize_width = 300
resize_height = 300
resized_gray_image = cv2.resize(gray_image, (resize_width, resize_height))
resized_bit_planes = [cv2.resize(plane, (resize_width, resize_height)) for plane in bit_planes]

cv2.imshow('Original Image', resized_gray_image)
for i, bit_plane in enumerate(resized_bit_planes):
    cv2.imshow(f'Bit Plane {i}', bit_plane)

cv2.waitKey(0)
cv2.destroyAllWindows()
