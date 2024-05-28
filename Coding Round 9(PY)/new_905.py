# Program to demonstrate Public, Private and Protected Access Modifiers/Specifiers

#1 Public  ----> Can be accessed from anywhere both in and outside the class

class Employee:

    def __init__(self,name,id):

        self.name = name
        self.id = id

    def display(self):

        print(f"The ID of {self.name} is {self.id}")


e1 = Employee("Kishore", 538)
e1.display()
print(e1.name)   # Here we are easily able to access the variables (name and id) from outside of the class 
print(e1.id)     # In Python By default all the variables are public. They can be accessed from anywhere 


