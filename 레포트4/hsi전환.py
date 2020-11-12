import cv2
import numpy as np
import math


def toHSI(img):
    row = img.shape[0]
    col = img.shape[1]

    new_img = np.zeros_like(img)

    for i in range(row):
        for j in range(col):
            r = int(img[i, j, 2])
            g = int(img[i, j, 1])
            b = int(img[i, j, 0])
            ii = (r+b+g)//3
            min_rgb = min(r, g, b)
            s = 1-(min_rgb/ii)
            temp = ((r-g)+(r-b))/(2*np.sqrt((r-g)*(r-g)+(r-b)*(g-b)))
            # print(temp)
            h = np.arccos(temp)*180/np.pi
            if b > g:
                h = 360-h
            # h /= 360
            new_img.itemset(i, j, 0, ii)
            new_img.itemset(i, j, 1, s)
            new_img.itemset(i, j, 2, h)
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
    hsi = toHSI(image)
    r, g, b = division(image)
    h, s, i = division(hsi)
    cv2.namedWindow('rgb', cv2.WINDOW_NORMAL)
    cv2.imshow('rgb', image)
    cv2.namedWindow('r', cv2.WINDOW_NORMAL)
    cv2.imshow('r', r)
    cv2.namedWindow('g', cv2.WINDOW_NORMAL)
    cv2.imshow('g', g)
    cv2.namedWindow('b', cv2.WINDOW_NORMAL)
    cv2.imshow('b', b)
    cv2.namedWindow('hsi', cv2.WINDOW_NORMAL)
    cv2.imshow('hsi', hsi)
    cv2.namedWindow('h', cv2.WINDOW_NORMAL)
    cv2.imshow('h', h)
    cv2.namedWindow('s', cv2.WINDOW_NORMAL)
    cv2.imshow('s', s)
    cv2.namedWindow('i', cv2.WINDOW_NORMAL)
    cv2.imshow('i', i)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
