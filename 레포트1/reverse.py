import cv2
import numpy as np
import toBinary


def imreverse(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, 255-img[x, y])    #255에서 빼서 반전시킴
    return new_img


if __name__ == '__main__':
    gray_src = toBinary.gray_imload('howell.jpg')       #그레이 이미지
    bin_img = toBinary.toBinary(gray_src)               #이진 이미지
    reversed_img = imreverse(gray_src)                  #그레이 이미지 반전
    re_bin_img = imreverse(bin_img)                     #이진 이미지 반전
    cv2.imshow('src', gray_src)
    cv2.imshow("bin_img", bin_img)
    cv2.imshow("reversed_img", reversed_img)
    cv2.imshow("reversed_bin_img", re_bin_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
