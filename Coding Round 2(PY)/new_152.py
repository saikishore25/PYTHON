# Other additional methods related to sets 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)      # Returns the Set with element which is common in the compared sets 

print(z)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)    # Comparision can be done with more 2 sets also 

print(result)



x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z1 = x1.union(y1)             # Returns the set which has both values which are comman in compared sets without repition 

print(z1)


x2 = {"a", "b", "c"}
y2 = {"f", "d", "a"}
z2 = {"c", "d", "e"}

result = x2.union(y2, z2)

print(result)