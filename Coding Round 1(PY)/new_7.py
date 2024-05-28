# Program to find the sum of individual digits entered 

number = int(input("Enter the Number Below: \n"))
sum = 0 
rem = 0 

while(number>0):

    rem = number % 10 
    sum = sum + rem
    number = number // 10


print("The Sum of Individual Digits of Number Entered is: ", sum)
