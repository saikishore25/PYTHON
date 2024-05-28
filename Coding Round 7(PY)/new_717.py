# 3. enumerate()
# IT RETURNS THE LIST OF ALL THREAD OBJECTS WHICH ARE CURRENTLY ALIVE 

from threading import * 


def display():

    for i in range(5):

        print("Hello")

def dont():

    for i in range(5):

        print("No")

t1 = Thread(target=display)
t1.start()

t2 = Thread(target=dont)
t2.start()


# print(enumerate())  # Gives all the threads as items in the form of TUPLE


for item in enumerate():

    print("The Thread is: ", item)

    