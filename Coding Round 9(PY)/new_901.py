# Introduction to Object Oriented Programming in Python 
# Implementing classes and objects 

class Computer:

    occupation = "Business"         # Declaring Variables (Static Declaration)
    Age = 19 
    

    def Configuration(self):        # Declaring  Methods 

        print("i5, 16GB, 1TB HDD")      # The above declared variables can be used inside the function too 
        print(f"he occupations is {self.occupation} and age is {self.Age}")



obj1 = Computer()
print(obj1.occupation)
print(type(obj1))
print(obj1.__dict__)

obj1.Configuration()                      # Both these syntaxes can be used to apply methods on objects 
Computer.Configuration(obj1)              

print(obj1.Age)

#######################################################################


obj2 = Computer()

obj2.Age = 21

print(obj2.Age)



