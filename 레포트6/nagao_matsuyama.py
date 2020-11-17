import cv2
import numpy as np
import openimg
import salt_pepper

mask=[[(0,0),(-2,-1),(-1,-1),(-2,0),(-1,0),(-2,1),(-1,1)],[(0,0),(-1,1),(-1,2),(0,1),(0,2),(1,1),(1,2)],[(0,0),(-1,-1),(-1,0),(-1,1),(-2,-1),(-2,0),(-2,1)],
        [(0,0),(-1,-1),(-1,-2),(0,-1),(0,-2),(1,-1),(1,-2)],[(0,0),(-2,-2),(-2,-1),(-1,-2),(-1,-1),(0,-1),(-1,0)],[(0,0),(-2,2),(-2,-1),(-1,2),(-1,1),(0,1),(-1,0)],
        [(0,0),(2,2),(2,1),(1,2),(1,1),(0,1),(1,0)],[(0,0),(2,-2),(2,-1),(1,-2),(1,-1),(1,0),(0,-1)]]


def nagao_matsuyama(img):
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
            e_bright=0
            f_bright=0
            g_bright=0
            h_bright=0
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if (i,j) in mask[0]:
                        a_bright+=img[x+i,y+j]
                    if (i,j) in mask[1]:
                        b_bright+=img[x+i,y+j]
                    if (i,j) in mask[2]:
                        c_bright+=img[x+i,y+j]
                    if (i,j) in mask[3]:
                        d_bright+=img[x+i,y+j]
                    if (i,j) in mask[4]:
                        e_bright+=img[x+i,y+j]
                    if (i,j) in mask[5]:
                        f_bright+=img[x+i,y+j]
                    if (i,j) in mask[6]:
                        g_bright+=img[x+i,y+j]
                    if (i,j) in mask[7]:
                        h_bright+=img[x+i,y+j]
            a_bright/=7
            b_bright/=7
            c_bright/=7
            d_bright/=7
            e_bright/=7
            f_bright/=7
            g_bright/=7
            h_bright/=7
            a_o,b_o,c_o,d_o,e_o,f_o,g_o,h_o=0,0,0,0,0,0,0,0
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if (i,j) in mask[0]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[1]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[2]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[3]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[4]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[5]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[6]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    if (i,j) in mask[7]:
                        a_o+=(img[x+i,y+j]-a_bright)*(img[x+i,y+j]-a_bright)
                    
            a_o/=7
            b_o/=7
            c_o/=7
            d_o/=7
            e_o/=7
            f_o/=7
            g_o/=7
            h_o/=7
            o=[a_o,b_o,c_o,d_o,e_o,f_o,g_o,h_o]
            b=[a_bright,b_bright,c_bright,d_bright,e_bright,f_bright,g_bright,h_bright]
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
    new_img = nagao_matsuyama(img)
    cv2.imshow('img', img)
    cv2.imshow('noise', noise)
    cv2.imshow('new_img', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
