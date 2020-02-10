from tkinter import *
root=Tk()
root.geometry("600x600")
mytext=StringVar()
def sqare():
    res=int(e1.get())*int(e1.get())
    mytext.set(res)
n1=Label(root,text="number").grid(row=0)
e1=Entry(root)
e1.grid(row=0,column=1)
b=Button(root,text="sqare",command=sqare).grid(row=2,column=3)
IbRES=Label(root,text="result",bg="yellow").grid(row=3)
Result=Label(root,textvariable=mytext).grid(row=3,column=1)







root.mainloop()