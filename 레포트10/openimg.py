import cv2
import numpy as np





def toGray(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, sum(img[x, y])//3)  # rgb값을 합쳐 3으로나눔

    return new_img


def gray_imload(path):  # 이미지로드
    return toGray(cv2.imread(path))



