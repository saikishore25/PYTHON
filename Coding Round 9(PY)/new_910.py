# Program to explain levels of Inheritance 
# 1 Single Inheritence 

class ParentClass:

    def __init__(self, name, age):

        self.name = name
        self.age = age 

    def display1(self):

        print(f"The Age of {self.name} is {self.age}")
        print("This is a Parent Class")


class ChildClass(ParentClass):

    def __init__(self, name, age, id):
        # self.name = name 
        # self.age = age       # Instead of rewriting evrything use the super() method
        # self.id = id 
        super().__init__(name, age)
        
        self.id = id


    def display2(self):
        print(f"The Age of {self.name} is {self.age} and his id is {self.id}")
        print("This is a Child Class")




e1 = ChildClass("kishore", 19, 434)
e1.display1()