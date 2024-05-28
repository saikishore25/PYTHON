# B. CREATE A THREAD WITHOUT EXTENDING THREAD CLASS 

from threading import * 

class Example:

    def display(self, n):

        for i in range(n):

            print("Hello World")


e1 = Example()
thread_object1 = Thread(target=e1.display(5,))
thread_object1.start()

for i in range(5):

    print("Welcome")


