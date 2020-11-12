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


def bitplane(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    imgs = []
    bit = 0b0000001         #8자리비트
    for _ in range(8):
        new_img = np.copy(img)

        for x in range(0, row):
            for y in range(0, col):
                new_img.itemset(x, y, img[x, y] & bit)          #&연산하여 하위 n비트획득
        imgs.append(new_img)                                    #비트플레인 획득
        bit <<= 1                   #왼쪽시프트하고
        bit += 1                    #1을더하여 하위비트를 1로채워나감

    return imgs


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    imgs = bitplane(img_src)            #비트플레인 리스트
    cv2.imshow('src', img_src)
    for i, j in enumerate(imgs):
        cv2.imshow(f'{i+1}bit', j)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
