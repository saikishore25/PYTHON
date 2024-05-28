# Program to explain file handling in python 


f1 = open("kishore.txt", "rt")   #reading
f2 = open("rajesh.txt", "wt")    #writing
f3 = open("suresh.txt", "at")    #append
print(f1.read())



f1.close()
f2.close()
f3.close()

f4 = open("kishore.txt", "r+t")   #reading and writing
f5 = open("rajesh.txt", "w+t")    #reading and writing
f6 = open("suresh.txt", "a+t")    #reading and appending

f4.close()
f5.close()
f6.close()

f7 = open("kishore.txt", "rb")   #reading in binary
f8 = open("rajesh.txt", "wb")    #writing in binary
f9 = open("suresh.txt", "ab")    #append in binary
print(f7.read())

f10 = open("kishore.txt", "r+b")   #reading and writing
f11 = open("rajesh.txt", "w+b")    #reading and writing
f12 = open("suresh.txt", "a+b")    #reading and appending
