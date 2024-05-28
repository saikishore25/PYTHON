# Program to implement the constructor method in python 

class Computer:

    def __init__(self, n, a):

        self.name = n
        self.age = a



    def Configuration(self):       

        
        print(f"His name is {self.name} and his age is {self.age}")


obj1 = Computer("kishore", 19)
print(obj1.__dict__)
obj1.Configuration()


obj2 = Computer("Ramesh", 29)
obj2.Configuration()

