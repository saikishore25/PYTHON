# 4. min 

import numpy as np 

arr1 = np.array([1,2,3,4])
print(arr1.min())
print(np.min(arr1))


arr2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr2.min())
print(np.min(arr2, axis=1))
print(np.min(arr2, axis=0))