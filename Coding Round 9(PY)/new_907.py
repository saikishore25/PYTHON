# 3 Protected   ----> Can be accessed in the main class and its inherited class and not outside 


class Person:
   
   def __init__(self, name, age):
      self._name = name    # Having a single underscore makes it private 
      self._age = age
    
   def _display(self):
      print("Name:", self._name)
      print("Age:", self._age)


class Person1(Person):
   
   def disc(self):
      
      print("Hello World")

e1 = Person("kishore", 16)

print(e1._name)

print(e1._age)


# Private variables can be normally accessed as public variables it is just a denotion to be used 




