# Program to understand aggregate functions in Python 
# 1. sum 

import numpy as np 

arr1 = np.array([1,2,3,4])
print(arr1.sum())
print(np.sum(arr1))


arr2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr2.sum())
print(np.sum(arr2, axis=1))
print(np.sum(arr2, axis=0))




