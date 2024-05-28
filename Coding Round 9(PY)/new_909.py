# Program to implement Inheritence in Python 

class Employee:

    def __init__(self, name, id):

        self.name = name 
        self.id = id

    def ShowDetails(self):

        print(f"The Name of the Employee is {self.name} and his id is {self.id}")

    
class Employee1(Employee):

    def __init__(self, name, id, age):

        self.name = name 
        self.id = id 
        self.age = age 

    def ShowLanguage(self):

        print(f"The ID of employee {self.name} aged {self.age} is {self.id}")
        








# e1 = Employee("Kishore", 438)
# e1.ShowDetails()

e2 = Employee1("ramesh", 423, 24)
e2.ShowLanguage()
# e2.ShowDetails()




