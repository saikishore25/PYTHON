# Program to understand super() function in Python 

class ParentClass:

    def __init__(self, name, id):
        self.name = name
        self.id = id 

    def parent_method(self):

        print("This is the Parent Method")
        print(f"The ID of {self.name} is {self.id}")

class ChildClass(ParentClass):

    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


    def child_method(self):

        print("This is the Child Class")
        print(f"The ID of employee {self.name} whose lang is {self.lang} is {self.id}")
        super().parent_method()            # We cannot directly call the method which was defined in parent class through its sub class but by using super() we can call parent class methods in child class
        # parent_method()       We cannot do this directly 

obj1 = ChildClass("kishore", 345, "Python")
obj1.parent_method()         # Here we can access the parentclass methods through child class objects 
obj1.child_method()


# By simply using super() we can access any method from anywhere 






