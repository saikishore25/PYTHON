# Read Content from one file and write it in another file

f1 = open("one.txt","w")
f1.write("Kishore is intelligent \n")
list_1 = ["apple \n", "orange \n"]
f1.writelines(list_1)

f1.close()

f2 = open("one.txt","r")
f3 = open("two.txt","w")

data1 = f2.readlines()

for i in data1:     # Here we are using loop as write method cannot take list as an argument

    f3.write(i)






