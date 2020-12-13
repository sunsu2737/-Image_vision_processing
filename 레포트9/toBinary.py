import cv2
import numpy as np


def gray_imload(path):  # 이미지로드
    return toGray(cv2.imread(path))


def toBinary(img, flag=125):      # 이미지 이진화
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)  # 이미지 복사
    for x in range(0, row):
        for y in range(0, col):
            if img[x, y] > flag:  # 임계값과 비교
                new_img.itemset(x, y, 255)
            else:
                new_img.itemset(x, y, 0)
    return new_img


def toGray(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, sum(img[x, y])/3)  # rgb값을 합쳐 3으로나눔

    return new_img


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    binary_img = toBinary(img_src, 100)  # 이진이미지
    cv2.imshow('src', img_src)

    cv2.imshow('binary', binary_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
