# Program to add text to An Image 

import numpy as np
import cv2


img = cv2.imread('car.jpg',1)

txt="FERRARI"
font = cv2.FONT_HERSHEY_SIMPLEX
# puttext(img, text, org, fontFace, fontScale, color, thickness)
cv2.putText(img,txt,(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
different font styles supported 

FONT_HERSHEY_SIMPLEX	0
FONT_HERSHEY_PLAIN	1
FONT_HERSHEY_DUPLEX	2
FONT_HERSHEY_COMPLEX	3
FONT_HERSHEY_TRIPLEX	4
FONT_HERSHEY_COMPLEX_SMALL	5
FONT_HERSHEY_SCRIPT_SIMPLEX	6
FONT_HERSHEY_SCRIPT_COMPLEX	7
FONT_ITALIC	16

'''