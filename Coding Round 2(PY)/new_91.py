# Program to find the Unique Elements in a  lIST 

def unique(list):

    new_list = []

    for i in list:

        c = list.count(i)

        if(c==1): 

            new_list.append(i)
    
    print("The Unique Elements in List are: ", new_list)




list1 = []
n = int(input("Enter the Number of Elements You Want in this List: "))

for i in range(0,n):
    
    element = int(input(f"Enter Element {i}: "))
    list1.append(element)

unique(list1)


