import cv2
import numpy as np
import openimg
import toBinary
import 침식
import 팽창


img = toBinary.toBinary(openimg.gray_imload("Lenna.png"))
new_img = 침식.chimsick(팽창.pangchang(img))

cv2.imshow("binary", img)
cv2.imshow("mopology", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
