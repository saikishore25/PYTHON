# Exception Handling in Python 
# A. try and except method 
# in this method if there is any erro which would might occur in our program, we put that in the try block if it executes perfectly its fine but if there is any exception it goes to the exception block where we explain what to do with the exception. 

# a = 5 
# b = 0

# try:                        

#     print(a/b)

# except Exception as E:

#     print("This is an error ", E)
#     b = int(input("Enter The Number Other Than Zero(0): "))



c = 54 
d = "true"

try:

    print(c/d)

except TypeError:   # By using in this way we can check if a particular is there in the program or not 

    print("This is a Type Error")



