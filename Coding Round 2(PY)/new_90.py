# Program to find the duplicate elements in a list 

def duplicate(list):
    
    duplicates = {}
    
    for item in list:

        c = list.count(item)

        if(c>=2):

            duplicates[item] = c 

    print("The Duplicate Elements are: ", duplicates)




lis1 = []
n = int(input("Enter the Number of Elements to be Inserted \n"))

for i in range(0,n):

    element = int(input(f"Element {i}: " ))
    lis1.append(element)



duplicate(lis1)
