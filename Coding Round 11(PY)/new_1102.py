# Program to read video file and display it 

import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('C:/Users/user/OneDrive/Documents/Programming/Python Language/Coding Round 11(PY)/videoo.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture the video frame-by-frame
  # read() - It returns two values 
  # 1. It returns the video frame as object by object like images 
  # 2. It returns a boolean value which states whether it sucessfully read the video or not 
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('d'):

        break

    # ord() - It takes a character as input and returns the ASCII CODE OF IT, whereas chr() - It takes a ASCII CODE as input and returns the character
 
  # Break the loop
  
 
# When everything done, release the video capture object
# This is automatically done but to free up the video caputring device which is webcam over here we need to do this manually 
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()