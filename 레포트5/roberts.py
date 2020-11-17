import cv2
import numpy as np
import openimg
import immask


def roberts_mask(mode=0):
    mask = [[[0, 0, -1], [0, 1, 0], [0, 0, 0]], [[-1, 0, 0],
                                                   [0, 1, 0], [0, 0, 0]]]
    return mask[mode]


if __name__ == '__main__':
    img = openimg.gray_imload('Lenna.png')

    new_img = immask.img_mask(img, roberts_mask(), 'embossing')
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

