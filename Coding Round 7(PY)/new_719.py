# Program to understand TID's, Native ID's, PID's 
# TID and Native ID are slightly different but for now they are showing same values we will learn the diference further 
# PID is completely different 

from threading import * 
import os


def kcpd():

    
    for i in range(5):

        print("Hello World")



def kmpd():

    
    for i in range(5):

        print("Welcome")



t1 = Thread(target=kcpd)
t1.start()       

t2 = Thread(target=kmpd)
t2.start()

print(t1.ident)
print(t1.native_id)
print(os.getpid())
