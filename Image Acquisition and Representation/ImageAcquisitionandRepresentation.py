import cv2
import numpy as np

# Görüntüyü oku
image = cv2.imread("ucak.jpg", cv2.IMREAD_COLOR)

# Görüntüyü göster
cv2.imshow("Original Image", image)

# Görüntü bilgilerini yazdır
print("Image Shape (Height, Width, Channels):", image.shape)
print("Image Data Type:", image.dtype)
print("Number of Pixels:", image.size)

# Belirli bir pikselin değerini yazdır
pixel = image[50, 120]
print(f"Pixel value at (50, 120): B={pixel[0]}, G={pixel[1]}, R={pixel[2]}")

# Pikseli değiştirme (260 yerine 255 kullanıldı)
image[50, 120] = [0, 255, 0]  # Yeşil renk değeri

# Değiştirilmiş görüntüyü göster
cv2.imshow("Modified Image", image)

# Değiştirilen görüntüyü kaydet
cv2.imwrite("modified_ucak.jpg", image)

# Tuşa basılana kadar bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
