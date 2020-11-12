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

def make_gray(img, level=200):      #한가지 레벨로가득찬 영상생성
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, level)
    return new_img


def imand(img1, img2):          #and연산
    row = max(np.shape(img1)[0], np.shape(img2)[0])
    col = max(np.shape(img1)[1], np.shape(img2)[1])
    new_img = np.copy(img1)

    for x in range(0, row):
        for y in range(0, col):
            new_img.itemset(x, y, img1[x, y] & img2[x, y])

    return new_img


def imor(img1, img2):       #or연산
    row = max(np.shape(img1)[0], np.shape(img2)[0])
    col = max(np.shape(img1)[1], np.shape(img2)[1])
    new_img = np.copy(img1)

    for x in range(0, row):
        for y in range(0, col):
            new_img.itemset(x, y, img1[x, y] | img2[x, y])

    return new_img


def imxor(img1, img2):  #xor연산
    row = max(np.shape(img1)[0], np.shape(img2)[0])
    col = max(np.shape(img1)[1], np.shape(img2)[1])
    new_img = np.copy(img1)

    for x in range(0, row):
        for y in range(0, col):
            new_img.itemset(x, y, img1[x, y] ^ img2[x, y])

    return new_img


if __name__ == '__main__':

    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    gray_img = make_gray(img_src)       # 단색 영상
    and_img = imand(img_src, gray_img)
    or_img = imor(img_src, gray_img)
    xor_img = imxor(img_src, gray_img)
    cv2.imshow('src', img_src)
    cv2.imshow('gray', gray_img)
    cv2.imshow('and_img', and_img)
    cv2.imshow('or_img', or_img)
    cv2.imshow('xor_img', xor_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
