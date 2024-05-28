# Changing the List Items 
# Adding Items to a list 

li1 = ["kishore", "ramesh", 1, "Apple", "4", 5, 3]
print(li1)

li1[3] = "Four"
print(li1)

li1[1:4] = ["kishore", "kumar", "varma"]   # Will insert the given values in the range of 1:4
print(li1)

li1[1:] = [1,2,3,4,5,6]      # Will insert the given values in the range of 1: last 
print(li1)

li1[1:3] = ["somu", "kumar", "rajesh"]   # Will increase the length of list when we entered items more than specified 
print(li1)

li1[-4:-2] = ["kummu", "kantu"]    # Will work same in negatie index also 
print(li1)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")                    # It inserts orange at the last position of the list
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(1, "orange")                # It inserts orange at the specified psotion 
print(thislist1)


thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)                  # THis method extends the elements of a list with other list 
print(thislist2)








