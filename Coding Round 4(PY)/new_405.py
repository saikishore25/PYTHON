# Program to verify readable(),writable(),isfile()  functions 
import os
f = open("rajesh.txt", "r+")
print(f.readable())  # Returns true if the file is readble according to mode
print(f.writable())  # Returns true if the file is writable according to mode
print(os.path.isfile("kis.txt"))


f.close()




