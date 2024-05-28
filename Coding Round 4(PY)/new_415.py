# Program to find the number of characters, words and lines in a File 

file_name = ("noi1.txt")
file = open(file_name, "r")

data = file.read()        # Returns the complete data from a file in string format 
# print(data)

no_characters = len(data)
no_words = len(data.split())
no_lines = len(data.splitlines())

print("The Number of Characters are: ", no_characters)
print("The Number of Words are: ", no_words)
print("The Number of Lines are: ", no_lines)


file.close()



