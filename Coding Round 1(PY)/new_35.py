# Program to print the factorial of a given number 


num = int(input("Enter the Number: "))

fact = 1 

for i in range(2,num+1):

    fact = fact*i


print("The Factorial of Entered Number is: ", fact)



