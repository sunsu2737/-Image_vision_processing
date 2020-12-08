import cv2
import numpy as np
import openimg
import math


def rotate(img, th=30):
    row, col = img.shape
    new_img = np.zeros((row, col), dtype=np.uint8)
    th = math.radians(th)
    r = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    c = np.array([[row//2], [col//2]])
    for x in range(row):
        for y in range(col):
            cur = np.array([[x], [y]])-c
            new = np.dot(r, cur)+c
            if 0 <= new[0, 0] < row and 0 <= new[1, 0] < col:
                new_img[x, y] = img[int(new[0, 0]), int(new[1, 0])]

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = rotate(img)

cv2.imshow("src", img)
cv2.imshow("rotate", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
