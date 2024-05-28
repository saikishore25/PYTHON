# Program to find contours of a given image 

import cv2 as cv 
import numpy as np 

img = cv.imread("Coding Round 11(PY)\car.jpg") 

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("IMAGE", img)

# Canny(variable of image, upper threshold, lower threshold)
canny = cv.Canny(img, 225, 175)

cv.imshow("IMAGE CANNY", canny)
cv.waitKey(0)

cv.destroyAllWindows()
