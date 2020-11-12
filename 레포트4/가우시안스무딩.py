import cv2
import numpy as np
import openimg
import immask


def gaussian_smooth_mask(mode=0):
    mask = [[[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]], [[1/273, 4/273, 7/273, 4/273, 1/273], [4/273, 16/273, 26/273, 16 /
                                                                                                            273, 4/273], [7/273, 26/273, 41/273, 26/273, 7/273], [4/273, 16/273, 26/273, 16/273, 4/273], [1/273, 4/273, 7/273, 4/273, 1/273]]]
    return mask[mode]


if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')
    new_img = immask.img_mask(img, gaussian_smooth_mask(1))
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
