# Program to understand image properties 

import cv2 as cv 

img = cv.imread(r"Coding Round 11(PY)\bike.jpg", 1)
print(img.shape)
print(img.size) # RETURNS THE SIZE OF IMAGE 
'''
The first two items shape[0] and shape[1] represent width and height of the image.
Shape[2] stands for a number of channels.
3 indicates that the image has Red Green Blue (RGB) channels.
'''