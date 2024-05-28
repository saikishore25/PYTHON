# 2. threading  - New module which has multiple synchronisation methods 
# Program to import threading module and verify main thread and another thread working 
# There are various ways to create a thread 
# After we click on RUN button Python Interpreter requests OS for creating a Main Thread to run the Program 
# There is always atleast one main thread/default thread which will be required to run the program 
# Python Virtual Machine Genarates this thread and runs the program 
# Whenever a new thread is created the PVM sends a request to OS and there scheduler allocates memory to run this thread 

# A. CREATE A THREAD WITHOUT USING ANY CLASS AND BY JUST USING FUNCTIONS 

from threading import *         # 1st step - IMPORT THREADING MODULE 

def newfunc():                  # 2nd Step - CREATE SOME FUNCTION 

    print("The Details of the thread executing this block is: \n", current_thread())
    for i in range(4):

        print("HELLO")


thread_obj = Thread(target=newfunc)        # 3rd step - ASSIGNING THE thread class TO AN OBJECT 
thread_obj.start()                          # 4th step - STARTING THE THREAD ( WITHOUT THIS THERE IS NO USE OF CREATING THREADS)

for i in range(5):

    print("Welcome")

print("The Details of the thread execting other block is: \n", current_thread())

# THE MAIN THREAD IS ALWAYS PRESENT IN A PROGRAM IRRESPECTIVE OF ITS MANUAL CREATION BY THE USER. IN CURRENT PROGRAM THERE ARE TWO THREADS 
# ONE WHICH WE CREATED AND OTHER IS MAIN THRED WHICH IS ALREADY EXISTING 

# def newfunc(n,msg):                  

#     for i in range(n):

#         print(msg)


# thread_obj = Thread(target=newfunc, args=(4, "HELLO"))        # here you can pass arguments as (args) into a tuple 
# thread_obj.start()                  




# def newfunc(n,msg):                  

#     for i in range(n):

#         print(msg)


# thread_obj = Thread(target=newfunc, kwargs={'n':4, 'msg':"HELLO"})        # here you can pass arguments as (kwargs) into a dictionary 
# thread_obj.start()                  
