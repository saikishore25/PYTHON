# Program to implement reading from files 

f1 = open("kishore.txt", "r") # File Pointer is set at the first letter of file
# print(f1.read(35))
print(f1.read())      #read() is used to read the whole data when no argument is specified
# print(f1.read())
# print(f1.readline(35))    #readline() is used to read a single line, reads the required number of characters from that particular line only


# print(f1.readlines())   # readlines() is used to read all the lines, it gives the content in a list

f1.close()






