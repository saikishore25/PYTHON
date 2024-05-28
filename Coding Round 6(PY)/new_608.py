# Program to verify various datatypes in numpy module 

import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1.dtype)   # integer



arr2 = np.array(["1","2","3"])
print(arr2.dtype)    #string


arr3 = np.array([1.44,3.22,4.60])
print(arr3.dtype)   #float 


arr4 = np.array([1,2,3,4,5], dtype=np.int16)
print(arr4.dtype)


