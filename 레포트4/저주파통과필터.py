import cv2
import numpy as np
import openimg
import immask


def highboost_mask(a=1):
    mask = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

    return mask


if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')

    new_img = immask.img_mask(img, highboost_mask(), 'highboost')
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
