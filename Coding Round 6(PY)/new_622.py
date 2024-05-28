# Slicing in 1,2,3 dimensional arrays 


import numpy as np 


arr1 = np.array([1,2,3,4,5,6])
print(arr1[0:4])       #[start:stop:stepvalue]
print(arr1[1:3])
print(arr1[1:5:2])
print(arr1[-3:-1])
print(arr1[-5:-1:2])

print()
arr2 = np.array([[1,4,3,5],[5,1,0,8],[7,6,3,1]])        # [row,column]
print(arr2)
print(arr2[0])
print(arr2[1:2,1])
print(arr2[1:3,1:3])
