# Program to apply certain pattern array methods

import numpy as np

x1= np.array(10)   # 0-D Array
print(x1)

x2 = np.array([10,20,30]) # 1-D Array 
print(x2)

x3 = np.array([[10,20,30],[40,50,60],[70,80,90]])  # 2-D Array 
print(x3)

x4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])   # 3-D Array 
print(x4)

########################################################################

x5 = np.zeros(1)   # zeros([rows, subrows, coloumns])
print(x5)

x6 = np.zeros(2)
print(x6)

x7 = np.zeros([3,3])
print(x7)

x8 = np.zeros([2,3,4])
print(x8)

########################################################################


x9 = np.full(3,1)
print(x9)

x10 = np.full([3,4], 5)
print(x10)

#######################################################################

x11 = np.ones(4)
print(x11)

x12 = np.ones((2,3))    # oness([rows, subrows, coloumns])
print(x12)

x13 = np.ones((3,4,5))
print(x13)

####################################################################3

x14 = np.arange(4)     #arange(range->0-n)
print(x14)

############################################################333333333333

x15 = np.eye(5)   # Prints the diagonal elements with 1 
print(x15)

###################################################################

x16 = np.linspace(2,10,num=4)        #linespace(start, end, number of elements)
print(x16)


