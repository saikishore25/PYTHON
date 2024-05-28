# c. CREATE A THREAD WITH EXTENDING THREAD CLASS 


from threading import * 

class Example(Thread):

    def run(self):

        for i in range(5):

            print("Hello World")


e1 = Example()
# thread_object1 = Thread(target=e1.display(5,))
e1.start()

for i in range(5):

    print("Welcome")