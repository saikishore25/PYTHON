# Program to explain Masking in open cv


import cv2 as cv 
import numpy as np

img = cv.imread("Coding Round 11(PY)\car.jpg")
cv.imshow("CAR IMAGE", img)

blank_image = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank_image)

circle = cv.circle(blank_image, (img.shape[0]//2, img.shape[1]//2), 100, 255, -1)
cv.imshow("Circle Image", circle)

bitwise_and = cv.bitwise_and(circle, img, mask= None )
cv.imshow("Masked Image", bitwise_and)

cv.waitKey(0)



