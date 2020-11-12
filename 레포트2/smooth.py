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

def smooth(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)


    nomal_hist = histo.nomarize(img)    #히스토그램 평활화

    for x in range(0, row):
        for y in range(0, col):
            new_img.itemset(x, y, round(nomal_hist[img[x, y]][0])) #픽셀을 평활화된 히스토그램으로 바꿈
    return new_img


if __name__ == '__main__':
    img_src = gray_imload("howell.jpg")  # 그레이 이미지
    smooth_img = smooth(img_src)  # 평활화된 이미지
    histo.draw_hist(histo.histo(img_src), histo.histo(smooth_img))
    cv2.imshow('src', img_src)
    cv2.imshow('smooth_img', smooth_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
