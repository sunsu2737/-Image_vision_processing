import cv2
import numpy as np
import openimg


def up_size(img):
    row, col = img.shape
    new_img = np.zeros((512, 512), dtype=np.uint8)

    for x in range(512):
        for y in range(512):
            new_img[x, y] = img[round(x/8), round(y/8)]

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = up_size(img[256:256+64+1, 256:256+64+1])

cv2.imshow("X1", img)
cv2.imshow("X8", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
