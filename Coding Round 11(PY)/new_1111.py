# Program to identify edges / contours in an image 

import cv2
import numpy as np

img = cv2.imread(r'Coding Round 11(PY)/car.jpg')
cv2.imshow('image',img)

# Canny(image object, lower Threshold value, upper threshold value)
imgcanny = cv2.Canny(img, 125, 175)
cv2.imshow("Canny Image", imgcanny)

#findcountours(canned image object, mode, method) - This method returns two values

# This returns all the contours in a list 
# Hierarchies of contours are returned

# mode 
# cv.RETR_EXTERNAL − Retrieves only the extreme outer contours.
# cv.RETR_LIST − Retrieves all of the contours without establishing any hierarchical relationships.
# cv.RETR_CCOMP − Retrieves all of the contours and organizes them into a twolevel hierarchy.
# cv.RETR_TREE − Retrieves all of the contours and reconstructs a full hierarchy of nested contours.

# method 

# cv.CHAIN_APPROX_NONE − Stores absolutely all the contour points.

# cv.CHAIN_APPROX_SIMPLE − Compresses horizontal, vertical, and diagonal segments and leaves only their end points.

contours, hierachies = cv2.findContours(imgcanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE ) 
print("The Number of Contours are", len(contours))
key=cv2.waitKey(0)

cv2.destroyAllWindows()

