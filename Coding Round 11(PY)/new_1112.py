# Program to implement IMAGE BITWISE OPERATIONS in PYthon 

import cv2 as cv 
import numpy as np 


# This is most used in cv2. Here this wil create a blank space and we can make it an image object(just remember)
blank = np.zeros((400,400), dtype="uint8")
cv.imshow("Blank Image", blank)         

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370), (255,255,255), -1)
cv.imshow("Rectangle", rectangle)

circle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)
cv.imshow("Circle", circle)



# INTERSECTING REGION IS RETURNED
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow("Bitwise AND", bitwise_and)

# INTERSECTING AND NON INTERSECTING REGIONS BOTH ARE RETURNED 
bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow("Bitwise OR", bitwise_or)

# NON INTERSECTING REGIONS ARE RETURNED
bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow("Bitwise XOR", bitwise_xor)

# IT RETURNS THE REGION NOT BELONGING TO CIRCLE
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT", bitwise_not_circle)

# IT RETURNS THE REGION NOT BELONGING TO RECTANGLE
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT", bitwise_not_circle)


cv.waitKey(0)
cv.destroyAllWindows()

