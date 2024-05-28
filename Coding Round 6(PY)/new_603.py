# Program to enter elements into an array at run time 

import numpy as np

li1 = []

for i in range(1,11):

    num_1 = int(input(f"Number{i}: "))
    li1.append(num_1)

print(np.array(li1))



