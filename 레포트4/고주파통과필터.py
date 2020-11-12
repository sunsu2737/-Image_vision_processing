import cv2
import numpy as np
import openimg
import immask


def highpass_mask():
    mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    return mask


if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')

    new_img = immask.img_mask(img, highpass_mask(), 'highpass')
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
