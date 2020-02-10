from tkinter import*
root=Tk()
root.geometry("600x500")
var1=IntVar()
Checkbutton(root,text='cricket',variable=var1).grid(row=0)
var2=IntVar()
Checkbutton(root,text='football',variable=var2).grid(row=1)

var3=IntVar()
Checkbutton(root,text='singing',variable=var3).grid(row=3)
root.mainloop()