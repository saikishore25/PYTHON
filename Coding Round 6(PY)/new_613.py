# 2. prod

import numpy as np 

arr1 = np.array([1,2,3,4])
print(arr1.prod())
print(np.prod(arr1))


arr2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr2.prod())
print(np.prod(arr2, axis=1))
print(np.prod(arr2, axis=0))
