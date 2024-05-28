# Program to implement Docorators in python 
# A decorator is something which takes a function as input and modifies it and returns the modified function

def decor(func1):

    def inner_decor():

        func1()

        print("Good Morning")

    return inner_decor


# def printer():

#     print("Good Morning")             # Method 1
#     print("Good Morning")

# result = decor(printer)
# result()


@decor
def printer():

    print("Good Morning")               # Method 2
    print("Good Morning")

printer()



