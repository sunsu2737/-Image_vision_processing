import cv2
import numpy as np
import openimg
import math


def rotate(img, a1, a2, a3, b1, b2, b3):
    row, col = img.shape
    new_img = np.zeros((row, col), dtype=np.uint8)
    r = np.array([[a1, a2], [b1, b2]])
    c = np.array([[a3], [b3]])
    for x in range(row):
        for y in range(col):
            cur = np.array([[x], [y]])
            new = np.dot(r, cur)+c
            if 0 <= new[0, 0] < row and 0 <= new[1, 0] < col:
                new_img[x, y] = img[int(new[0, 0]), int(new[1, 0])]

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = rotate(img, 1.2, -0.4, 0, 0, 1, 0)

cv2.imshow("src", img)
cv2.imshow("rotate", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
