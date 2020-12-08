import openimg
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = openimg.gray_imload("Lenna.png")
row, col = img.shape
mask = np.zeros((row, col), np.uint8)
mask[row-270:row+270, col-270:col+270] = 1
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift2 = fshift.copy()
fshift[row-290:row+290, col-290:col+290] = 0
fshift2 = fshift2*mask

iff = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift)))
iff2 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift2)))

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(iff, cmap='gray')
plt.title('hipass'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(iff2, cmap='gray')
plt.title('lowpass'), plt.xticks([]), plt.yticks([])

plt.show()
