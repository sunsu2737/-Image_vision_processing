import cv2
import numpy as np
import openimg
import math


def up_size(img,):
    row, col = img.shape
    new_img = np.zeros((512, 512), dtype=np.uint8)

    for x in range(512):
        for y in range(512):

            bb = x/8-x//8
            aa = y/8-y//8
            a, b, c, d = img[x//8, y//8], img[x//8, y //
                                              8+1], img[x//8+1, y//8], img[x//8+1, y//8+1]
            p1 = (a*(1-aa)+b*aa)
            p2 = (c*(1-aa)+d*aa)
            new_img[x, y] = p1*(1-bb)+p2*(bb)

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = up_size(img[256:256+64+1, 256:256+64+1])

cv2.imshow("X1", img)
cv2.imshow("X8", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
