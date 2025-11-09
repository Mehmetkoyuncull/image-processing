import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_matching(original_image, reference_image):
    original_hist, _ = np.histogram(original_image.flatten(), bins=np.arange(6), density=True)
    reference_hist, _ = np.histogram(reference_image.flatten(), bins=np.arange(6), density=True)

    original_cdf = np.cumsum(original_hist)
    reference_cdf = np.cumsum(reference_hist)

    original_cdf_normalized = original_cdf / original_cdf.max()
    reference_cdf_normalized = reference_cdf / reference_cdf.max()

    original_mapping = np.round(original_cdf_normalized * 3).astype(int)
    reference_mapping = np.round(reference_cdf_normalized * 3).astype(int)

    matched_image = np.zeros_like(original_image)
    for i in range(5):
        matched_image[original_image == i] = reference_mapping[i]

    return matched_image, original_mapping, reference_mapping

def plot_image_and_histogram(ax, image, title):
    ax[0].imshow(image, cmap='gray', interpolation='nearest')
    ax[0].set_title(title)
    ax[1].hist(image.flatten(), bins=np.arange(6) - 0.5, edgecolor='black', density=True)
    ax[1].set_title("Histogram")
    ax[1].set_xlabel("Pixel Value")
    ax[1].set_ylabel("Frequency")

original_image = cv2.imread('kop.jpg', cv2.IMREAD_GRAYSCALE)
reference_image = np.array([
    [4, 3, 2, 3, 2],
    [2, 2, 3, 4, 4],
    [1, 2, 3, 2, 2],
    [3, 3, 3, 1, 4],
    [1, 2, 3, 4, 4]
])

matched_image, _, _ = histogram_matching(original_image, reference_image)

fig, axs = plt.subplots(3, 2, figsize=(18, 18))

plot_image_and_histogram(axs[0], original_image, "Original Image")
plot_image_and_histogram(axs[1], reference_image, "Reference Image")
plot_image_and_histogram(axs[2], matched_image, "Matched Image")

for i in range(3):
    axs[i, 0].axis('off')

plt.tight_layout()
plt.show()
