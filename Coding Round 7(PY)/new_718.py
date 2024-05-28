# 4. join()
# Eventhought the execution time is getting reduced we still have some irregularities in the output 
# this irregularities can be prevented when we use join()

# IT BLOCKS THE EXECUTION OF OTHER CODE UNTILL THE THREAD ON WHICH THE JOIN() IS APPLIED GETS TERMINATED 

from threading import * 

def display():

    for i in range(5):

        print("Hello")


def show():

    for i in range(5):

        print("Go")

t1 = Thread(target=display)

t1.start()
t1.join()           # After everytime we start a thread we can use join method to perfectly execute the code.

t2 = Thread(target=show)

t2.start()
t2.join()

for i in range(5):

    print("come")



