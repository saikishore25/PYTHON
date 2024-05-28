# Program to understand how threading reduces the time of executing a program 
# A. Program without using MULTITHREADING 

from threading import * 
import time 

def square(num):
    
    print("Finding Square...")
    time.sleep(1)
    print(f"The Square of {num} is: ", num**2)

def cube(num):
    
    print("Finding Cube...")
    time.sleep(1)
    print(f"The Cube of {num} is: ", num**3)



begin_time = time.time()

square(5)

cube(5)


print("The Time taken for execution: ", time.time()-begin_time)


