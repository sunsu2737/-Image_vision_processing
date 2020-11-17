import cv2
import numpy as np
import openimg


def minus(img):  # 유사 연산자
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)

    for x in range(1, row-1):  # 마스크형태로 픽셀들을 연산
        for y in range(1, col-1):
            new_pixel = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    new_pixel = max(abs(img[x+i, y+i]-img[x-i, y - j]), new_pixel)
            # print(int(new_pixel),end=' ')

            new_img.itemset(x, y, new_pixel+50)

        # print()
    return new_img


if __name__ == '__main__':
    img = openimg.gray_imload('Lenna.png')

    new_img = minus(img)
    cv2.imshow('img', img)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
