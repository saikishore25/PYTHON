#Program to verify File Object Variables and  few important arguments in open function 

f = open("ni.txt", "r",buffering=2,encoding="UTF-8")

print("File Name is: ", f.name)
print("File Encoding is: ", f.encoding)
print("File Mode is: ", f.mode)
print("Is File Closed: ", f.closed)
print(f.read())

f.close()



