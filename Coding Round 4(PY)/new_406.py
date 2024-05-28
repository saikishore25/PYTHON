# Program to verify tell() and seek() methods in python

f = open("kishore.txt", "r")
print(f.tell())   #tell() function returns the current position of the cursor in the text file
print(f.read(6))
print(f.tell())
print(f.seek(0))    #seek() functions sets the position of cursor at the required place you want in the file

print(f.read())



f.close()

