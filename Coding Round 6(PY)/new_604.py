# Program to initialize dimensional Arrays 

import numpy as np

arr1 = np.array(2)
print(arr1)
print(type(arr1))
print(arr1.ndim)


arr2 = np.array([1,2,3,4,5,6])
print(arr2)
print(type(arr2))
print(arr2.ndim)

arr3 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(arr3)
print(type(arr3))
print(arr3.ndim)

arr4 = np.array([[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]],[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]])
print(arr4)
print(type(arr4))
print(arr4.ndim)



