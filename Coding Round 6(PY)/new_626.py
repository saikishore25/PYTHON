# Program to understand Concatination in Arrays 

import numpy as np

# 1-D ARRAYS 

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array([6,7,8,9,0])
print(arr2)

arrconcat = np.concatenate((arr1,arr2), axis=0)  # By default if axis is not mentioned it is considered as 0

print(arrconcat)


# 2-D ARRAYS 

arr3 =  np.array([[2,3,4,5],[6,5,3,2],[1,2,3,4]])
print(arr3)

arr4 = np.array([[1,5,6,7],[5,0,3,4],[3,2,1,0]])
print(arr4)

arr1concat = np.concatenate((arr3,arr4), axis=0)
print(arr1concat)

arr2concat = np.concatenate((arr3,arr4), axis=1)
print(arr2concat)

# 3-D ARRAYS 


arr4 = np.array([[[1,2,3],[1,2,2]],[[1,5,6],[4,0,9]]])
print(arr4)

arr5 = np.array([[[5,4,0],[1,2,3]],[[0,8,7],[5,1,9]]])
print(arr5)

arr3concat = np.concatenate((arr4,arr5), axis=0)
print(arr3concat)

arr4concat = np.concatenate((arr4,arr5), axis=1)
print(arr4concat)