from tkinter import *
root=Tk()
root.geometry("600x200")
Label(root,text="hello").grid(row=0,column=2)
Entry(root).grid(row=1,column=1)
Button(root,text="click here").place(x=140,y=150)




root.mainloop()