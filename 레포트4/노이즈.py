import cv2
import numpy as np
import openimg
import immask


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


def highboost_mask(mode=0):
    mask = [ [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],[[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]], [[1/256, 4/256, 6/256, 4/256, 1/256], [4/256, 16/256, 24/256,
        16/256, 4/256], [6/256, 24/256, 36/256, 24/256, 6/256], [4/256, 16/256, 24/256, 16/256, 4/256], [1/256, 4/256, 6/256, 4/256, 1/256]]]


    return mask[0]


if __name__ == '__main__':
    img = openimg.gray_imload('howell.jpg')
    noise_img = add_gaussian(img)
    new_img = immask.img_mask(noise_img, highboost_mask())
    cv2.imshow('img', img)
    cv2.imshow('noise', noise_img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
