import cv2
import numpy as np


def gray_imload(path):  # 이미지로드
    return toGray(cv2.imread(path))
    
def toGray(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, sum(img[x, y])/3)     #rgb값을 합쳐 3으로나눔

    return new_img


def imadd(img1, img2, a=0.5):
    row = max(np.shape(img1)[0], np.shape(img2)[0])
    col = max(np.shape(img1)[1], np.shape(img2)[1])
    new_img = np.copy(img1)

    for x in range(0, row):
        for y in range(0, col):
            new_pixel = (1-a)*img1[x, y]+(a)*img2[x, y]  # 가중치 합
            new_img.itemset(x, y, new_pixel)


    return new_img


if __name__ == '__main__':
    img_src1 = gray_imload("howell.jpg")  # 그레이 이미지
    img_src2 = gray_imload("bigwell.jpg")  # 그레이 이미지

    add_img = imadd(img_src1, img_src2)

    cv2.imshow('src1', img_src1)
    cv2.imshow('src2', img_src2)
    cv2.imshow('add_img', add_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
