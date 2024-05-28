# Program to change the color of background and foreground on mouse click 


from tkinter import* 

root = Tk()

b1 = Button(root, text="Kishore", activebackground="blue", activeforeground="black")
b1.pack(side=RIGHT)
b2 = Button(root, text="Rajesh", activebackground="blue", activeforeground="yellow")
b2.pack(side=LEFT)
b3 = Button(root, text="Kishore", activebackground="blue", activeforeground="yellow")
b3.pack(side=TOP)
b4 = Button(root, text="Rajesh", activebackground="blue", activeforeground="yellow")
b4.pack(side=BOTTOM)

root.mainloop()