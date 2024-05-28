# OpenCV Module
# pip install opencv-contrib-python ---> Extra Methods for use 
# pip install opencv-python ---> Main basic methods for use 
# PROGRAM TO READ AN IMAGE USING THIS MODULE 

import cv2 as cv 

# imread(file path, flag) - This reads the specified image and returns the image. Here flag specifies the color format 
# flag 1 - IMREAD_COLOR 
# flag 2 - IMREAD_GRAYSCALE 
# flag 3 - IMREAD_ANYCOLOR

img = cv.imread("Coding Round 11(PY)\car.jpg") 

# imshow(gui title, variable of image) - This method shows the image in newly created interface
cv.imshow("IMAGE", img)

# This method waits for the specified milliseconds of time and then closes the window
cv.waitKey(0)

cv.destroyAllWindows()
