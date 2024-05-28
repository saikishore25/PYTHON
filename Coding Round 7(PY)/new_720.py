# Program to change names of threads 

from threading import * 

def kcpd():

    
    for i in range(5):

        print("Hello World")

print("Total Number of Active Threads1 : ", active_count())

def kmpd():

    
    for i in range(5):

        print("Welcome")

print("Total Number of Active Threads2 : ", active_count())

t1 = Thread(target=kcpd)
t1.name = "S-Thread-1"         # Like this we can change the name of other working threads 
print(t1.name)
t1.start()

current_thread().name = "S-MainThread-1"            # Like this we can change the name of the current thread 
print("The Thread1 is: ", current_thread().name)


t2 = Thread(target=kmpd)
t2.start()

print("The Thread2 is: ", current_thread().name)

print("The Total Number of Active Threads are3 : ", active_count())