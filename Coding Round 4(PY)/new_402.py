# Program to impliment writing in files 

f1 = open("kishore.txt", "w")
f1.write("Kishore is intelligent person fuck is the new sex of tehc kdsjdksjdksjdksjdskjdskdjskdjs")   # write() is used 
li1 = ["Kishore", "is", "an", "Intelligent", "Person", "As", "Raju", "Is", "Not\n"]
f1.writelines("rajesh")    #writelines() is used to write some content into the file you want to 
f1.writelines(li1)

f1.close()