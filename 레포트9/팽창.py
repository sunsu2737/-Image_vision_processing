import cv2
import numpy as np
import openimg
import toBinary

def pangchang(img):
    row, col = img.shape
    new_img = np.zeros((512, 512), dtype=np.uint8)

    for x in range(1,row-1):
        for y in range(1,col-1):
            if img[x-1,y-1]==img[x-1,y]==img[x-1,y+1]==img[x,y-1]==img[x,y]==img[x,y+1]==img[x+1,y-1]==img[x+1,y]==img[x+1,y+1]==0:
                new_img[x, y] = 0
            else:
                new_img[x,y]=255

    return new_img

if __name__ == '__main__':
    img = toBinary.toBinary(openimg.gray_imload("Lenna.png"))
    new_img = pangchang(img)

    cv2.imshow("binary", img)
    cv2.imshow("mopology", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
