import cv2
import numpy as np
import openimg
import salt_pepper


def a_trimmend(img, a=0.5):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)

    for x in range(1, row-1):  # 마스크형태로 연산
        for y in range(1, col-1):
            members = []
            new_pixel = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    members.append(img[x+i, y+j])  # 중간값을찾는다.
            members.sort()
            cut = int(a*9)
            new_pixel = sum(members[cut:9-cut])/(9-cut*2)
            # print(int(new_pixel),end=' ')

            new_img.itemset(x, y, new_pixel)

        # print()
    return new_img


if __name__ == '__main__':
    img = openimg.gray_imload('Lenna.png')
    noise = salt_pepper.salt_pepper(img)
    new_img = a_trimmend(img, 0.2)
    cv2.imshow('img', img)
    cv2.imshow('noise', noise)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
