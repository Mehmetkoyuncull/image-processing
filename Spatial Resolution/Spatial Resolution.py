import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


custom_image = cv2.imread('sarac.jpg', cv2.IMREAD_GRAYSCALE)


plt.imshow(custom_image, cmap='gray')
plt.show()


if custom_image is not None:

    line_sum = np.sum(custom_image, axis=0)


    peaks, _ = find_peaks(line_sum, height=0.5)

    peak_distances = np.diff(peaks)


    mm_per_image = 10
    pixels_per_mm = custom_image.shape[1] / mm_per_image


    spatial_resolution = pixels_per_mm / np.mean(peak_distances)

    print(f"Spatial Resolution: {spatial_resolution:.2f} LP/mm")
else:
    print("Görüntü yüklenemedi veya geçerli formatta değil.")
