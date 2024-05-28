# Program to explain 
# try except else finally blocks 

print("Start")

try:

    print("Try Block")
    x = int(input("Enter the Number1: "))
    y = int(input("Enter Number2: "))
    z = x/y 

except Exception as E:     # This gets executed only if try block has an exception

    print("The Exception is: ", E)

else:           # This gets executed only if try block doesnt have any exception

    print("The Division is: ", z)

finally:         # This block will be executed irrespective of the outcomes of the other blocks 

    print("We are out of all blocks")



