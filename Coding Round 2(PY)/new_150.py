#3. SET 
# unordered, unchangeable, No duplicate values, unindexed 

set1 = {}         # By default this curly braces denote a dict 
print(type(set1))

set2 = {"kishore","ramesh"}
set3 = {1,2,3,4,5}
set4 = {"kishore", "ramesh", True, 1, "4"}
print(set4)     # This can be printed in any order as it doesn't have any indexing 

print(type(set2))


set5 = set(("kishore", "r", 1, 3))     # This is a set constructor 
print(type(set5))
