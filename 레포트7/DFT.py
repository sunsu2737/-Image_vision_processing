import cv2
import numpy as np
import openimg




def dft(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]

    G = np.zeros((row, col), dtype=np.complex)



    print(row,col)


    for l in range(row):
        print(l)
        for k in range(col):
            v = 0
            for n in range(row):
                for m in range(col):
                    v += img[n, m] * np.exp(-2j * np.pi * (m * k / row + n * l / col))
            G[l, k] = v 

    return G




def idft(img):
    row = np.shape(img)[0]
    col = np.shape(img)[1]

    G = np.zeros((row, col), dtype=np.complex)



    print(row,col)


    for l in range(row):
        print(l)
        for k in range(col):
            v = 0
            for n in range(row):
                for m in range(col):
                    v += img[n, m] * np.exp(-2j * np.pi * (m * k / row + n * l / col))
            G[l, k] = v/(row*col)

    return G



img = openimg.gray_imload("Lenna.png")


G = dft(img)
iG= idft(G)



cv2.imshow("img", img)
cv2.imshow("G", G)
cv2.imshow("iG",iG)
cv2.waitKey(0)
cv2.destroyAllWindows()
