#Program to understand copy() and view()

import numpy as np 

#1 copy()
# It owns the data 
# it gives a new array 
# changes made to original are not reflected in the copy 

arr1 = np.array([1,4,3,4])
copy = arr1.copy()
arr1[2] = 6
print(arr1)
print(copy)



#2 view()
# It doesnt own the data 
# it gives the original array 
# changes made to original are reflected in the copy 

arr2 = np.array([1,4,3,4])
view = arr2.view()
arr2[2] = 8
print(arr2)
print(view)
