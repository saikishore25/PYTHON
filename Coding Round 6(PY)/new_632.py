#2 searchsorted()- It searches for the correct position to fit in the given number so that the order doesnt break 


import numpy as np 

# 1-D ARRAYS 

arr1 = np.array([1,2,5,6,10,15])
print(arr1)
x = np.searchsorted(arr1,7)     # RETURNS THE INDEX VALUE OF THE INSERTED POSITION
print(x)

arr2= np.array([1,5,7,20,25])
print(arr2)
y = np.searchsorted(arr2, [9,4,23], side='right')   # By default it starts to search from the left side but when gave the argument as right it wil search from right 

print(y)

# 2-D ARRAYS 

