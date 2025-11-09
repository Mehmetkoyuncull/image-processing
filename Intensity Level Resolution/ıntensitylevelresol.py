import cv2
import numpy as np

image = cv2.imread('elma.jpg', cv2.IMREAD_GRAYSCALE)

print(f"Veri tipi: {image.dtype}")
print(f"Min yoğunluk: {np.min(image)}")
print(f"Max yoğunluk: {np.max(image)}")

normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

normalized_image = np.uint8(normalized_image)

cv2.imshow('Normalize Edilmiş Görüntü', normalized_image)

image_16bit = np.uint16(image) * 256

# Yeni 16-bit görüntü aralığını kontrol et
print(f"16-bit görüntü - Min yoğunluk: {np.min(image_16bit)} Max yoğunluk: {np.max(image_16bit)}")

normalized_16bit_image = cv2.normalize(image_16bit, None, 0, 255, cv2.NORM_MINMAX)
normalized_16bit_image = np.uint8(normalized_16bit_image)


cv2.imshow('16-bit Normalize Edilmiş Görüntü', normalized_16bit_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
