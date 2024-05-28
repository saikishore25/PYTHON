# Program to implement random number array methods 

# 1. rand(row, subrow, coloumn) - gives only positive values between 0 and 1

import numpy as np

y = np.random.rand(3)
print(y)

y1 = np.random.rand(3,4)
print(y1)

y2 = np.random.rand(2,3,4)
print(y2)

######################################################################

# 2. randn(row, subrow, coloumn) - it prints both positive and negative numbers between 0 and 1

y3 = np.random.randn(4)      
print(y3)

y4 = np.random.randn(3,4)
print(y4)

y5 = np.random.randn(2,3,4)
print(y5)

#####################################################################

# 3. randint(min, max, total number of values in array) - it prints the values between a given range 

y6 = np.random.randint(4,10,4)  
print(y6)


# 4. ranf(row, subrow, coloumn) - it prints both positive and negative numbers between 0.0 and 1.0

y7 = np.random.randint(2)
print(y7)
