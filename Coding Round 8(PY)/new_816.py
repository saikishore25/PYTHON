# Program to understand Frames and Parenting in Python 
# Frames are empty and invisibe untill you add some widgets inside them 

from tkinter import* 

root = Tk()
# root.geometry("600x400")
root.title("Frames & Parenting")

frame1 = Frame(root, height=100, width=200, bg="yellow", bd=20, relief=SUNKEN)
frame1.pack()

# label1 = Label(root, text="Outside the frame")
# label1.pack(side=RIGHT)                               # In the master parameter we need to give the frame name in which we want to add other widgets so that they remain intact 

label2 = Label(frame1, text="Inside the frame")
label2.pack()

label3 = Label(frame1, text="Inside the Frame")
label3.pack()




root.mainloop()