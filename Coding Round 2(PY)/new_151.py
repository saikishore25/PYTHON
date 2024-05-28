# Program to add or remove items from a set 
# Once a set is created we cannot change the item we can only add or remove 

set1 = {"kishore", "rajesh", 1, False, None}

set1.add("orange")      # This adds an element into a set 
print(set1)

set2 = {"apple", 1, 2, 3}

set1.update(set2)       # This concatinates two sets 

set1.update("kum")   # It can also concatinate a string into set

print(set1)


