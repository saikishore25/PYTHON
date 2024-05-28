# 2. Multiple Inheritence 

class Employee:
    
    def __init__(self, name, id):

        self.name = name 
        self.id = id 

class Dancer:

    def __init__(self, type):

        self.type = type 

class EmployeeDancer(Employee, Dancer):

    pass


