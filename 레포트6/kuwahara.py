import cv2
import numpy as np
import openimg
import salt_pepper


def kuwahara(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)

    for x in range(-2, row-2):  # 마스크형태로 연산
        for y in range(-2, col-2):
            new_pixel = 0
            a_bright=0
            b_bright=0
            c_bright=0
            d_bright=0
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if i<=0 and j<=0:
                        a_bright+=img[x+i,y+j]
                    if i<=0 and j>=0:
                        b_bright+=img[x+i,y+j]
                    if i>=0 and j<=0:
                        c_bright+=img[x+i,y+j]
                    if i>=0 and j>=0:
                        d_bright+=img[x+i,y+j]
            a_bright/=9
            b_bright/=9
            c_bright/=9
            d_bright/=9
            a_o,b_o,c_o,d_o=0,0,0,0
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if i<=0 and j<=0:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if i<=0 and j>=0:
                        b_o+=(img[x+i,y+j]-b_bright)*(img[x+i,y+j]-b_bright)
                    if i>=0 and j<=0:
                        c_o+=(img[x+i,y+j]-c_bright)*(img[x+i,y+j]-c_bright)
                    if i>=0 and j>=0:
                        d_o+=(img[x+i,y+j]-d_bright)*(img[x+i,y+j]-d_bright)
            a_o/=9
            b_o/=9
            c_o/=9
            d_o/=9
            b=[a_bright,b_bright,c_bright,d_bright]
            o=[a_o,b_o,c_o,d_o]
            idx=0
            t_min=9999999
            for i,t in enumerate(o):
                if t_min>t:
                    t_min=t
                    idx=i
                        

                    

            # print(int(new_pixel),end=' ')

            new_img.itemset(x, y, b[idx])

        # print()
    return new_img


if __name__ == '__main__':
    img = openimg.gray_imload('Lenna.png')
    noise = salt_pepper.salt_pepper(img)
    new_img = kuwahara(img)
    cv2.imshow('img', img)
    cv2.imshow('noise', noise)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
