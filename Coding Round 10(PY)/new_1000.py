# Program to print x to n Numbers using Recursions 


def numton(start,num):
    
    if (start>num):
        return 

    print(start)
    numton(start+1,num)




start = int(input("Enter the Start Number: "))
num = int(input("Enter the End Number: "))

print("The Pattern is as follows: \n")
numton(start,num)
