# Program to add images in python 

from tkinter import * 
from PIL import ImageTk, Image

# PIL - Python Imaging Library 
# ImageTk - It is used to import jpg images into the window screen 
# This method supports any type of image formats to be seen 

root = Tk()
root.title("Photo Viewer")

myimage = ImageTk.PhotoImage(file="C:/Users/user/OneDrive/Desktop/digi.png")
mylabel = Label(image=myimage)
mylabel.pack()

image_one = ImageTk.PhotoImage(file="C:/Users/user/OneDrive/Desktop/digi.png")
image_two = ImageTk.PhotoImage(file="C:/Users/user/OneDrive/Desktop/tree-736885_1280.jpg")  
new1_label = Label(root, image=image_one)
new2_label = Label(root,image=image_two )
new1_label.pack()
new2_label.pack()

root.mainloop()



