# Program to resize an image 

def resizeframe(frame, scale=0.65):

    height = int(frame.shape[0] * scale) # shape is a property which containes height and width of an image in tuple format
    width = int(frame.shape[1] * scale)
    
    dimensions = (height, width)

    # resize(src, dsize, dst, fx, fy, interpolation)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)



import cv2 as cv 

img = cv.imread("Coding Round 11(PY)\car.jpg") 


cv.imshow("IMAGE", img) # ORIGINAL IMAGE 

img2 = resizeframe(img)

cv.imshow("RESIZED IMAGE", img2)

cv.waitKey(0)

cv.destroyAllWindows()
