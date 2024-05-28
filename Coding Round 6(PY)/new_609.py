# Program to understand the indexing of an array 

import numpy as np 

arr1 = np.array(0)
print(arr1)
print(type(arr1))


arr2 = np.array([1,2,3,4,5])    # BOTH POSITIVE AND NEGATIVE INDEXING IS ALLOWED 
print(arr2)
print(arr2[3])
print(arr2[-2])


arr3 = np.array([[1,2,3,4],[8,93,4,3],[4,2,0,1]])        # BOTH POSITIVE AND NEGATIVE INDEXING IS ALLOWED 
print(arr3)
print(arr3[1,1])
print(arr3[-2,-3])


arr4 = np.array([[[1,2,3,4],[5,6,7,8],[5,6,7,8]],[[1,5,6,7],[5,4,0,7],[1,3,0,4]]])       # BOTH POSITIVE AND NEGATIVE INDEXING IS ALLOWED 
print(arr4)
print(arr4[1,2,2])
print(arr4[-1,-3,-4])



