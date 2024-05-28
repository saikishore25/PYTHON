# Program to implement modify methods of string 

str1 = "  Kishore is intelligent "
str2 = "Ramesh, is, intelligent"
mytup = ("John", "Wick", "Baba Yaga")
print(str1.upper())         # Converts a string into upper case
print(str1.lower())         # Converts a string into lower case
print(str1.strip())         # Removes whitespaces before and after and returns trimmed string
print(str1.replace("K", "se"))
print(str1.replace(str1, str2))
print(str1.split())        # splits the string based on separator and stores in a list
print(str2.split(','))
print(str1.count("is"))
print(str1.find("e",4,10))  # search e in between the positions 4 and 10 
x = "#".join(mytup)
print(x)
print(type(x))
print(str1.title())  #capitalize each word

str3 = '''Kishore is intelligent and is
 the most handsome man alive on this planet'''

x3 = str3.splitlines()   # This breaks the string at newline and adds it as an item to a list 

print(x3)