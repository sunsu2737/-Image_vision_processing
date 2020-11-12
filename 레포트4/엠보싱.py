import cv2
import numpy as np
import openimg
import immask


def embossing_mask(mode=0):
    mask = [[[-1, -1, 0], [-1, 0, 1], [0, 1, 1]], [[-1, 0, 0],
                                                   [0, 0, 0], [0, 0, 1]], [[1, 0, 0], [0, 0, 0], [0, 0, -1]]]
    return mask[mode]


if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')

    new_img = immask.img_mask(img, embossing_mask(), 'embossing')
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
