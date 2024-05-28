# Some Functions used in Iterations 
# 1. nditer() - This functions is used to iterate over larger dimensional arrays without using multiple looping statements 

import numpy as np 

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1)

for i in np.nditer(arr1):

    print(i)

print()

arr2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(arr2)

for i in np.nditer(arr2):

    print(i)

   


arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[5,4,3,2],[3,0,5,6]]])
print(arr3)

for i in np.nditer(arr3):

    print(i)


    

