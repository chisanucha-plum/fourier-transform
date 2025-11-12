from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmKTFI_7r2TKR0sknfK_7GJX8sHItxbf-zh_jOJIBde2-L69K29IAzFLrD&s"

response = requests.get(url)
img_data = response.content

img = Image.open(BytesIO(img_data))
img_gray = np.array(img.convert("L"))

# Compute FFT
f = np.fft.fft2(img_gray)
fshift = np.fft.fftshift(f)

# Magnitude spectrum (add small eps to avoid log(0))
eps = 1e-8
magnitude_spectrum = 20 * np.log(np.abs(fshift) + eps)

# low-pass filter
rows, cols = img_gray.shape
crow, ccol = rows // 2, cols // 2
radius = 30  # radius of the low-pass filter in pixels (adjustable)
Y, X = np.ogrid[:rows, :cols]
distance = np.sqrt((Y - crow) ** 2 + (X - ccol) ** 2)
mask = np.zeros((rows, cols), np.uint8)
mask[distance <= radius] = 1

# Apply mask and inverse FFT
fshift_masked = fshift * mask
f_ishift = np.fft.ifftshift(fshift_masked)
image_filtered = np.fft.ifft2(f_ishift)
image_filtered = np.abs(image_filtered)

# Normalize filtered image for display
image_filtered_norm = (image_filtered - image_filtered.min()) / (
    (image_filtered.max() - image_filtered.min()) + eps
)

# Plot original, magnitude spectrum, and filtered image
plt.figure(figsize=(15, 6))
plt.subplot(1, 3, 1)
plt.imshow(img_gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Magnitude Spectrum")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(image_filtered_norm, cmap="gray")
plt.title("Low-Pass Filtering")
plt.axis("off")

# Save result
output_path = r"c:\chisanucha\image processing\fft_lowpass_result.png"
plt.tight_layout()
plt.savefig(output_path, dpi=150)
print(f"Saved result to: {output_path}")
plt.show()
