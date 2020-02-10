from tkinter import*
root=Tk()
root.geometry("499x600")
var=IntVar()
Radiobutton(root,text="male",variable=var,value=1).grid(row=0)
Radiobutton(root,text='female',variable=var,value=2).grid(row=1)
root.mainloop()
