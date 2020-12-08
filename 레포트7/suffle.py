import openimg
import cv2
import numpy as np
from matplotlib import pyplot as plt

def fft(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]

    G = np.zeros((row, col), dtype=np.complex)

    print(row, col)

    for l in range(row):
        print(l)
        for k in range(col):
            v = 0
            for n in range(row):
                for m in range(col):
                    v += img[n, m] * \
                        np.exp(-2j * np.pi * (m * k / row + n * l / col))
            G[l, k] = v

    return G

def ifft(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]

    G = np.zeros((row, col), dtype=np.complex)

    print(row, col)

    for l in range(row):
        print(l)
        for k in range(col):
            v = 0
            for n in range(row):
                for m in range(col):
                    v += img[n, m] * \
                        np.exp(-2j * np.pi * (m * k / row + n * l / col))
            G[l, k] = v/(row*col)

    return G

img = openimg.gray_imload("Lenna.png")
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum1 = 20*np.log(np.abs(f))
magnitude_spectrum2 = 20*np.log(np.abs(fshift))

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(magnitude_spectrum1, cmap='gray')
plt.title('fft'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(magnitude_spectrum2, cmap='gray')
plt.title('fft_suffle'), plt.xticks([]), plt.yticks([])
plt.show()
