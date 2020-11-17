import cv2
import numpy as np
import openimg
import immask
import laplacian
import 가우시안스무딩

if __name__ == '__main__':
    img = openimg.gray_imload('Lenna.png')
    

    new_img = immask.img_mask(img,가우시안스무딩.gaussian_smooth_mask())-immask.img_mask(img,가우시안스무딩.gaussian_smooth_mask(1))
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()