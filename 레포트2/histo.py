import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


def draw_hist(*histograms):     #히스토그램을 그리는함수

    num=1
    for hist in histograms:
        plt.figure(num)
        data = hist[0:-1, 0]
        bins = hist[0:-1, 1]
        plt.xlim(-20,275)
        plt.bar(bins, data)
        num+=1

    plt.show()


def histo(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    histogram = np.zeros((256, 2), int)
    for x in range(row):
        for y in range(col):
            histogram[img[x, y]][0] += 1  # 빈도수추가
            histogram[img[x, y]][1] = img[x, y]  # 인덱스

    return histogram


def real(img):
    histogram = histo(img)
    return histogram[histogram[:, 0] > 0, :]  # 실제로 이미지에 있는값만 추출


def hist_sum(img):  # 누적합 히스토그램
    histogram = histo(img)
    new_histogram = np.zeros((256, 2), int)
    c_sum = 0                           #누적합
    for i in range(256):
        c_sum += histogram[i][0]
        new_histogram[i][0] = c_sum
        new_histogram[i][1] = i

    return new_histogram


def nomarize(img):  # 평활화된 히스토그램
    sum_histo = hist_sum(img)
    real_hist = real(img)
    max_gray = real_hist[-1][1]  # 최대그레이레벨
    size = sum_histo[-1][0]  # 영상 크기
    new_histogram = np.zeros((256, 2), int)
    for i in range(256):
        new_histogram[i][0] = sum_histo[i][0]/size*max_gray  # 공식
        new_histogram[i][1] = i

    return new_histogram


def make_desire(img, hilight=122):  # 강조하고싶은 부분의 히스토그램
    sum_hist = hist_sum(img)
    size = sum_hist[-1][0]
    new_histogram = np.zeros((256, 2), int)     
    divide = size//255              #전체 개수를 스케일로나눔

    for i in range(256):            #전체영역에 고르게 분포시킴
        new_histogram[i][0] = divide
        new_histogram[i][1] = i
    num = 0
    flag = 0
    for i in range(hilight, -1, -1):    #기준값왼쪽을깎아냄

        new_histogram[i][0] -= flag
        for j in range(i, hilight+1):
            new_histogram[j][0] += flag//(hilight-i+1)
        if flag+math.log(num+1,2) < divide:
            num += 1
            flag += math.log(num, 2)
    num = 0
    flag = 0
    hilight += 1
    for i in range(hilight, 256):       #기준값 오른쪽을 깎아냄

        new_histogram[i][0] -= flag
        for j in range(i, hilight-1, -1):
            new_histogram[j][0] += flag//(i-hilight+1)
        if flag+math.log(num+1,2) < divide:
            num += 1
            flag += math.log(num, 2)
    return new_histogram


def real_H(histogram):
    return histogram[histogram[:, 0] > 0, :]  # 실제로 이미지에 있는값만 추출


def hist_sum_H(histogram):  # 누적합
    new_histogram = np.zeros((256, 2), int)
    c_sum = 0
    for i in range(256):
        c_sum += histogram[i][0]
        new_histogram[i][0] = c_sum
        new_histogram[i][1] = i

    return new_histogram


def nomarize_H(histogram):  # 평활화된 히스토그램
    sum_histo = hist_sum_H(histogram)
    real_hist = real_H(histogram)
    max_gray = real_hist[-1][1]  # 최대그레이레벨
    size = sum_histo[-1][0]  # 영상 크기
    new_histogram = np.zeros((256, 2), int)
    for i in range(256):
        new_histogram[i][0] = sum_histo[i][0]/size*max_gray  # 공식
        new_histogram[i][1] = i

    return new_histogram


def lookup(desired_histo):

    nomarize_histo = nomarize_H(desired_histo)
    new_histogram = np.zeros((256, 2), int)

    for i in range(256):        #평활화된 히스토그램을 이용해 역변환을위한 룩업 테이블을 만듬
        if nomarize_histo[i][0] > 0:
            new_histogram[nomarize_histo[i][0]][0] = nomarize_histo[i][1]
            new_histogram[nomarize_histo[i][0]][1] = nomarize_histo[i][0]
            new_histogram[nomarize_histo[i][0]-1][0] = nomarize_histo[i][1]-1
            new_histogram[nomarize_histo[i][0]-1][1] = nomarize_histo[i][0]-1

    return new_histogram
