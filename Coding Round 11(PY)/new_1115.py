# Program to detect Face 


import cv2 as cv 
import numpy as np 

img = cv.imread("Coding Round 11(PY)\indian.jpg")
cv.imshow("Team Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Team", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of Faces Found are {len(faces_rect)}")

for(x,y,w,h) in faces_rect:

    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)

cv.imshow("Detection", img)

