import cv2
import numpy as np


def toCMY(img):
    row = img.shape[0]
    col = img.shape[1]

    new_img = np.zeros((row, col, 3), np.uint8)

    for i in range(row):
        for j in range(col):
            c = 255-img[i, j, 2]
            m = 255-img[i, j, 1]
            y = 255-img[i, j, 0]

            new_img.itemset(i, j, 0, y)
            new_img.itemset(i, j, 1, m)
            new_img.itemset(i, j, 2, c)
    return new_img

def division(img):
    row = img.shape[0]
    col = img.shape[1]

    b_img = np.zeros((row, col, 3), np.uint8)
    g_img = np.zeros((row, col, 3), np.uint8)
    r_img = np.zeros((row, col, 3), np.uint8)
    for i in range(row):
        for j in range(col):
            b_img.itemset(i,j,0,img[i,j,0])
            g_img.itemset(i,j,1,img[i,j,1])
            r_img.itemset(i,j,2,img[i,j,2])
    return r_img,g_img,b_img



if __name__ == '__main__':

    image = cv2.imread('Lenna.png')
    cmy = toCMY(image)
    r,g,b=division(image)
    c,m,y=division(cmy)
    cv2.namedWindow('rgb',cv2.WINDOW_NORMAL)
    cv2.imshow('rgb',image)
    cv2.namedWindow('r',cv2.WINDOW_NORMAL)
    cv2.imshow('r',r)
    cv2.namedWindow('g',cv2.WINDOW_NORMAL)
    cv2.imshow('g', g)
    cv2.namedWindow('b',cv2.WINDOW_NORMAL)
    cv2.imshow('b', b)
    cv2.namedWindow('cmy',cv2.WINDOW_NORMAL)
    cv2.imshow('cmy',cmy)
    cv2.namedWindow('c',cv2.WINDOW_NORMAL)
    cv2.imshow('c', c)
    cv2.namedWindow('m',cv2.WINDOW_NORMAL)
    cv2.imshow('m', m)
    cv2.namedWindow('y',cv2.WINDOW_NORMAL)
    cv2.imshow('y', y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
