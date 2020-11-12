import cv2
import numpy as np
import toBinary


def correction(img,r=2.5):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range(row):
        for y in range(col):
            new_img.itemset(x, y, min(255, img[x, y]*r))          #감마값을 곱하여 밝기를 조절한다
    return new_img


if __name__ == '__main__':
    gray_src = toBinary.gray_imload('howell.jpg')           #그레이 이미지
    correct_img = correction(gray_src)                      #밝기조절된 이미지
    cv2.imshow('src', gray_src)
    cv2.imshow("correct_img", correct_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
