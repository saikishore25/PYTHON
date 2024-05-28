#max 

import numpy as np 

arr1 = np.array([1,2,3,4])
print(arr1.max())
print(np.max(arr1))


arr2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr2.max())
print(np.max(arr2, axis=1))
print(np.max(arr2, axis=0))
