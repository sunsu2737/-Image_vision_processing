import cv2
import numpy as np
import math


def toYCbCr(img):
    row = img.shape[0]
    col = img.shape[1]

    new_img = np.zeros_like(img)

    for i in range(row):
        for j in range(col):
            r = img[i, j, 2]
            g = img[i, j, 1]
            b = img[i, j, 0]
            y = 16+65.738*r/256+129.057*g/256+25.064*b/256
            cb = 128-37.945*r/256-74.494*g/256+112.439*b/256
            cr = 128+112.439*r/256-94.154*g/256-18.285*b/256
            new_img.itemset(i, j, 0, cr)
            new_img.itemset(i, j, 1, cb)
            new_img.itemset(i, j, 2, y)
    return new_img


def division(img):
    row = img.shape[0]
    col = img.shape[1]

    b_img = np.zeros((row, col, 3), np.uint8)
    g_img = np.zeros((row, col, 3), np.uint8)
    r_img = np.zeros((row, col, 3), np.uint8)
    for i in range(row):
        for j in range(col):
            b_img.itemset(i, j, 0, img[i, j, 0])
            g_img.itemset(i, j, 1, img[i, j, 1])
            r_img.itemset(i, j, 2, img[i, j, 2])
    return r_img, g_img, b_img


if __name__ == '__main__':

    image = cv2.imread('Lenna.png')
    ycbcr = toYCbCr(image)
    r, g, b = division(image)
    y, cb, cr = division(ycbcr)
    cv2.namedWindow('rgb', cv2.WINDOW_NORMAL)
    cv2.imshow('rgb', image)
    cv2.namedWindow('r', cv2.WINDOW_NORMAL)
    cv2.imshow('r', r)
    cv2.namedWindow('g', cv2.WINDOW_NORMAL)
    cv2.imshow('g', g)
    cv2.namedWindow('b', cv2.WINDOW_NORMAL)
    cv2.imshow('b', b)
    cv2.namedWindow('ycbcr', cv2.WINDOW_NORMAL)
    cv2.imshow('ycbcr', ycbcr)
    cv2.namedWindow('y', cv2.WINDOW_NORMAL)
    cv2.imshow('y', y)
    cv2.namedWindow('cb', cv2.WINDOW_NORMAL)
    cv2.imshow('cb', cb)
    cv2.namedWindow('cr', cv2.WINDOW_NORMAL)
    cv2.imshow('cr', cr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
