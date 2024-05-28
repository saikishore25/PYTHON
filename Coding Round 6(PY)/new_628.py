# Program to understand split function 

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

newarr = np.array_split(arr1, 3)

print(newarr)
print(newarr[2])    # To get the required array which we splitted 


import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr1 = np.array_split(arr, 3)

print(newarr1)