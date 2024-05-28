# Program to check whether given number is prime or not 

number = int(input("Enter the Number below: \n"))
count = 0
for i in range(1,number):

    if(number%i==0):

        count += 1


if(count>2):

    print("It is not a Prime Number \n")

else:

    print("It is a Prime")

