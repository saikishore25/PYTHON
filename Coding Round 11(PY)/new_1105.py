# Program To store an image in another format or change an image and store it again
# cv2.imwrite(filename, image object) method is used to save an image to any storage device. This will save the image according to the specified format in current working directory.


import numpy as np
import cv2


# Load an color image in grayscale
img = cv2.imread(r'Coding Round 11(PY)\bike.jpg',0)
cv2.imshow('image',img)

key=cv2.waitKey(0)

if key==ord('s'):
   
   cv2.imwrite(r"Coding Round 11(PY)\bike2.jpg", img)

   
cv2.destroyAllWindows()