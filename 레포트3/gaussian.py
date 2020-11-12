import cv2
import numpy as np


def add_gaussian(img, std=20):

    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range(row):
        for y in range(col):
            std_norm = np.random.normal()  # 평균0 분산1의 랜덤한값 생성
            random_noise = std*std_norm  # 기준값과 곱해 노이즈생성
            new_pixel = img[x, y]+random_noise  # 영상에 노이즈 삽입
            if 0 <= new_pixel <= 255:
                new_img[x, y] = new_pixel
    return new_img


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
def sub_gaussian(img, cycle=8):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    pixel = [[0]*col for _ in range(row)]
    for i in range(cycle):  # 노이즈영상 여러개를 합침
        noize = add_gaussian(img)
        for x in range(0, row):
            for y in range(0, col):
                pixel[x][y] += noize[x, y]

    for x in range(0, row):  # 합친만큼나눠 노이즈제거
        for y in range(0, col):
            new_img.itemset(x, y, pixel[x][y]//8)
    return new_img


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    img_noize = add_gaussian(img_src)  # 노이즈 삽입
    img_subnoize = sub_gaussian(img_src)  # 노이즈제거
    cv2.imshow('src', img_src)
    cv2.imshow('noize', img_noize)
    cv2.imshow('subnoize', img_subnoize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
