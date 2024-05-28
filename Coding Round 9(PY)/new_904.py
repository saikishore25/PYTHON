# Inbuilt Functions to implement of classes and objects 


class Demo:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display(self):

        print("hii")

obj1 = Demo("kishore", 19)


#1 hasattr(obj_name, attribute_name) - It returns TRUE if the class has the named attribute in it 


print(hasattr(obj1, "name"))
print(hasattr(obj1, "kumar"))


#2 getattr(obj_name, attribute_name, default) - It returns the value of the named attribute 

print(getattr(obj1, "name"))
print(getattr(obj1, "koinahi", 19))



#3 setattr(obj_name, attribute_name, attribute_value) - It helps to add new attribute to the class 

setattr(obj1, "occupation", "business")
print(obj1.name)
print(obj1.age)
print(obj1.occupation)      # This attribute is set with the help of setattr()


# delattr(obj_name, attribute_name)  - It deletes the named attribute and its value 

delattr(obj1, "name")
# print(obj1.name)            # The object name is deleted 


# isinstance(obj_name, class_name) - It is used to check whether the given object is an instance of the class or not 

print(isinstance(obj1, Demo))


# issubclass()



