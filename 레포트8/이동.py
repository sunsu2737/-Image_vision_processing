import cv2
import numpy as np
import openimg


def move(img,dx=150,dy=150):
    row, col = img.shape
    new_img = np.zeros((512, 512), dtype=np.uint8)
    

    for x in range(max(dx,0),min(row,row+dx)):
        for y in range(max(dy,0),min(col,col+dy)):
            if 0<=x-dx<row and 0<=y-dy<col:
                new_img[x, y] = img[x-dx,y-dy]

    return new_img


img = openimg.gray_imload("Lenna.png")
new_img = move(img)

cv2.imshow("src", img)
cv2.imshow("move", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
