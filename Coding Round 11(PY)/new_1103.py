# Python program to explain cv2.cvtColor() method 

# importing cv2 
import cv2 

# path 
path = r'C:\Users\user\OneDrive\Documents\Programming\Python Language\Coding Round 11(PY)\car.jpg'

# Reading an image in default mode 
src = cv2.imread(path) 



# Using cv2.cvtColor(image variable, color_change) method 
# Using cv2.COLOR_BGR2GRAY color space 
# conversion code 
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY ) 

# Displaying the image 
cv2.imshow("Image", image) 


cv2.waitKey(0)