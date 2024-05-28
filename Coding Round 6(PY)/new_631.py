# Program to understand searching operations in Arrays 
# 1. where()
import numpy as np 

# 1-D ARRAYS 

arr1 = np.array([1,2,3,4,5,5,2,1])
print(arr1)

x = np.where(arr1==2)  # We can put up any expression inside the parameter 
print(x)

y = np.where(arr1%2 == 0)       # RETURNS THE INDEX VALUES OF ARRAY
print(y)


# 2-D ARRAYS 
