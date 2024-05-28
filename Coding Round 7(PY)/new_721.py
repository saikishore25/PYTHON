# Program to understand how threading reduces the time of executing a program 
# A. Program by using MULTITHREADING 

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

t1 = Thread(target=square, args=(5,))

t2 = Thread(target=cube, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()

print("The Time taken for execution: ", time.time()-begin_time)


