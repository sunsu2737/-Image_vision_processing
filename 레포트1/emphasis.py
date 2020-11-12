import cv2
import numpy as np
import toBinary


def emphasis(img, low=128, high=192):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range(row):
        for y in range(col):
            if low <= img[x, y] <= high:            #강조할 범위에 들어가면 강조
                new_img.itemset(x, y, 255)
    return new_img


if __name__ == '__main__':
    gray_src = toBinary.gray_imload('howell.jpg')       #그레이이미지
    em_img = emphasis(gray_src)                         #부분강조된 이미지

    cv2.imshow('src', gray_src)
    cv2.imshow("em_img", em_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
