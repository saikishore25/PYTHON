#3 mean 

import numpy as np 

arr1 = np.array([1,2,3,4])
print(arr1.mean())
print(np.mean(arr1))


arr2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr2.mean())
print(np.mean(arr2, axis=1))
print(np.mean(arr2, axis=0))

