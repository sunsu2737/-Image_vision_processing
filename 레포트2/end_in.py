import cv2
import numpy as np
import histo


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

def end_in(img, low_f=20, high_f=200):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    histogram = histo.histo(img)

    real_hist = histo.real(img)

    low = real_hist[0, 1]  # 가장 낮은값
    high = real_hist[-1, 1]  # 가장 높은값

    for x in range(0, row):
        for y in range(0, col):

            if low_f <= img[x, y] <= high_f:
                new_pixel = (img[x, y]-low)/(high-low)*255  # 공식
                new_img.itemset(x, y, new_pixel)
            elif img[x, y] < low_f:  # 최저임계값
                new_img.itemset(x, y, 0)
            elif high_f < img[x, y]:  # 최대임계값
                new_img.itemset(x, y, 255)
    return new_img


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    end_in_img = end_in(img_src)

    histo.draw_hist(histo.histo(img_src), histo.histo(end_in_img))

    cv2.imshow('src', img_src)
    cv2.imshow('stretching_img', end_in_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
