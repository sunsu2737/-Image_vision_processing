import cv2
import numpy as np
import openimg
import math


def scale(img, mag=2):
    row, col = img.shape
    new_img = np.zeros((row*mag-mag, col*mag-mag), dtype=np.uint8)

    for x in range(row*mag-mag):
        for y in range(col*mag-mag):

            bb = x/mag-x//mag
            aa = y/mag-y//mag
            a, b, c, d = img[x//mag, y//mag], img[x//mag, y //
                                                  mag+1], img[x//mag+1, y//mag], img[x//mag+1, y//mag+1]
            p1 = (a*(1-aa)+b*aa)
            p2 = (c*(1-aa)+d*aa)
            new_img[x, y] = p1*(1-bb)+p2*(bb)

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = scale(img)

cv2.imshow("src", img)
cv2.imshow("scale", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
