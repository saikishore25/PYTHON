# Program to ITERATE over arrays

import numpy as np 

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1)

for i in arr1:

    print(i)

print()

arr2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(arr2)

for i in arr2:

    for j in i:

        print(j)


arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[5,4,3,2],[3,0,5,6]]])
print(arr3)

for i in arr3:

    for j in i:

        for k in j:

            print(k)

