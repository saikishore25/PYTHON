# Program to understand  LabelFrame and Frames in Python 


from tkinter import * 

root = Tk()
root.geometry("1050x800")

label_frame = LabelFrame(root, text="This is mainframe system",padx=50, pady=40)
label_frame.pack()

label1 = Label(label_frame,text="kishore")
label1.pack()



root.mainloop()
