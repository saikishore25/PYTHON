# Program to print Factorial of a number 

def fact(n):
    
    if n==0 or n==1:
        return 1
    
    return n*fact(n-1)




x = int(input("Enter the Number to print Factorial: "))

FACTORIAL = fact(x)

print(FACTORIAL)