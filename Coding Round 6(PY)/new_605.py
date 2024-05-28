# Program to create arrays and find their dimensions

import numpy as np

x1= np.array(10)   # 0-D Array
print(x1)

x2 = np.array([10,20,30]) # 1-D Array 
print(x2)

x3 = np.array([[10,20,30],[40,50,60],[70,80,90]])  # 2-D Array 
print(x3)

x4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])   # 3-D Array 
print(x4)

print(x1.ndim)       #ndim gives us the dimension of an array 
print(x2.ndim)
print(x3.ndim)
print(x4.ndim)

print(x2[0])
print(x3[0][2])    
print(x4[0][1][1])  
print(x3[1][-2])
print(x4[2][1][-3])     #Negative Indexing is allowed


