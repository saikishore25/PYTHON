# Program to create an array 


import numpy as np

arr1 = np.array([1,2,3,4,5,6]) # Passing a list into an Array 
print(arr1)
print(type(arr1))

arr2 = np.array((1,2,3,4,5,6))  # Passing a tuple into an Array 
print(arr2)
print(type(arr2))
print(arr2[2])


arr3 = np.array({1,2,3,4,5,6})  # Passing a set into an Array 
print(arr3)
print(type(arr3))
# print(arr3[2])

arr4 = np.array({1:"Kishore",2:"Rajesh"})  #Passing a Dictionary into an Array 
print(arr4)
print(type(arr4))
# print(arr4[2])


# We can pass any iterable object into the array function 



