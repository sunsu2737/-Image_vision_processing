import cv2
import numpy as np
import openimg
import immask


def blurring_mask(mode=0):  #블러링 마스크
    mask=[[[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],[[1/25, 1/25, 1/25,1/25,1/25],[1/25, 1/25, 1/25,1/25,1/25],[1/25, 1/25, 1/25,1/25,1/25],[1/25, 1/25, 1/25,1/25,1/25],[1/25, 1/25, 1/25,1/25,1/25]]]
    return mask[mode]
if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')
    new_img = immask.img_mask(img, blurring_mask(1))
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
