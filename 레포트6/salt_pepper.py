import cv2
import numpy as np


def salt_pepper(img,per=10):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.copy(img)
    for x in range((row*col)//100*per):
        r=np.random.randint(0,row)
        c=np.random.randint(0,col)
        s_p=np.random.randint(0,2)
        if s_p==0:
            new_img[r,c]=0
        else:
            new_img[r,c]=255

    return new_img

