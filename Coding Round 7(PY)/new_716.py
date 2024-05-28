# Different Built in Methods present in Python Multithreading 
# 2. active_count() 
# IT RETURNS THE NUMBER OF THREADS ALIVE FOR THE CURRENT RUNNING PROGRAM 

from threading import * 
import time 

def kcpd():

    print("Child Thread: ", current_thread().name)
    for i in range(5):

        print("Hello World")

print("Total Number of Active Threads: ", active_count())

def kmpd():

    print("Child Thread: ", current_thread().name)
    for i in range(5):

        print("Welcome")

print("Total Number of Active Threads: ", active_count())

t1 = Thread(target=kcpd)
t1.start()

print("Total Number of Active Threads: ", active_count())

t2 = Thread(target=kmpd)
t2.start()


print("Total Number of Active Threads: ", active_count())

print("Main Thread: ", current_thread().name)

for i in range(5):

    print("Fuckk Off")

print("Total Number of Active Threads: ", active_count())


