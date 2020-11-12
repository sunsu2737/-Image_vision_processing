import cv2
import numpy as np
import histo
import smooth


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
def toGray(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, sum(img[x, y])/3)     #rgb값을 합쳐 3으로나눔

    return new_img

def specification(img, desire):     #명세화
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    lookuptable = histo.lookup(desire)          #룩업테이블생성

    for x in range(0, row):
        for y in range(0, col):
            if lookuptable[img[x, y]][0] != 0:
                new_img.itemset(x, y, lookuptable[img[x, y]][0])#룩업테이블에 매칭시켜 명세화된 히스토그램을얻음
    return new_img


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    smooth_img = smooth.smooth(img_src)  # 평활화된 이미지
    desired_hist = histo.make_desire(img_src)       #원하는형태의 히스토그램

    spec_img = specification(smooth_img, desired_hist)  
    histo.draw_hist(histo.histo(img_src), desired_hist, histo.histo(spec_img))
    cv2.imshow('src', img_src)

    cv2.imshow('spec_img', spec_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
