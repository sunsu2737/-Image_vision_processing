import cv2
import numpy as np

def img_mask(img, mask,mode='nomal'):       #마스킹을위한 함수
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    new_img = np.zeros((row, col), np.uint8)

    for x in range(len(mask)//2, row-len(mask)//2): #마스크를이용하여 영상을 마스킹한다
        for y in range(len(mask)//2, col-len(mask)//2):
            new_pixel = 0
            for i in range(len(mask)):
                for j in range(len(mask)):
                    new_pixel += img[x+i-len(mask)//2, y+j-len(mask)//2]*mask[i][j]
            # print(int(new_pixel),end=' ')
            if mode=='highpass':        #모드에따라 추가연산을한다
                new_pixel+=img[x,y]
            if mode=='embossing':
                new_pixel+=80
            if mode=='highboost':
                new_pixel=img[x,y]-new_pixel
                new_pixel+=img[x,y]
            new_pixel=min(max(0,new_pixel),255)
            new_img.itemset(x, y, new_pixel)

        # print()
    return new_img
