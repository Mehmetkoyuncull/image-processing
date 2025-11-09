import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("zurafa.jpg", cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow("Original Image", image)

# Downsample the image
downsampled_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_AREA)
cv2.imshow("Downsampled Image", downsampled_image)

# Upsample the image back to the original size
upsampled_image = cv2.resize(downsampled_image, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Upsampled Image", upsampled_image)

# Function to quantize the image
def quantize_image(img, levels):
    max_val = 255
    step = max_val // levels
    quantized_img = (img // step) * step
    quantized_img = np.clip(quantized_img, 0, max_val)  # Ensure pixel values are within valid range
    return quantized_img.astype(np.uint8)  # Convert to uint8 for correct display and saving

# Quantize the image with 4 levels
quantized_image = quantize_image(image, 4)
cv2.imshow("Quantized Image (4 Levels)", quantized_image)

# Save the images
cv2.imwrite("downsampled_example.jpg", downsampled_image)
cv2.imwrite("upsampled_example.jpg", upsampled_image)
cv2.imwrite("quantized_example.jpg", quantized_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
