# Program to understand SORT FUNCTIONS IN ARRAYS 
# sort() - It sorts by default in ascending order ( numericals, aplhabets, strings)


# 1-D ARRAY 

import numpy as np

arr1 = np.array([3, 2, 0, 1])
print(np.sort(arr1))

arr2 = np.array(['a','h','K','L','g'])  # Captials are placed first 
print(np.sort(arr2))

arr3 = np.array(["kishore", "rajesh", "suresh"])
print(np.sort(arr3))



# 2-D ARRAY 


arr4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr4))

