# Program to perform basic ARITHMETIC OPERATIONS ON ARRAYS 
# 1-D 

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,4,3,2])

# with constant

conadd = arr1 + 4 
print(conadd)

consub = arr1 - 4 
print(consub)

conmulti = arr1*4
print(conmulti)

condiv = arr1/4
print(condiv)

conmod = arr1%2
print(conmod)

conpower = arr1**2
print(conpower)

# with another array 

arradd = arr1 + arr2
print(arradd)

arrsub = arr1 - arr2 
print(arrsub)

arrmulti = arr1*arr2
print(arrmulti)

arrdiv = arr1/arr2
print(arrdiv)

arrmod = arr1%arr2
print(arrmod)

arrpower = arr1**arr2
print(arrpower)