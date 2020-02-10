from tkinter import *
root=Tk()
root.geometry("600x500")
addno=StringVar()

e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)



def add():
    res1 = int(e1.get())+int(e2.get())
    addno.set(res1)


n1=Label(root,text="num1").grid(row=0)
n2=Label(root,text="num2").grid(row=1)



n3=Label(root, text="Result:",bg="yellow").grid(row=3)
result=Label(root,textvariable=addno).grid(row=3,column=1)




b=Button(root,text="add",command=add).grid(row=2,column=1)



root.mainloop()
# mytext=StringVar()
# def sqare():
#     res=int(e1.get())*int(e1.get())
#     mytext.set(res)
# n1=Label(root,text="number").grid(row=0)
# e1=Entry(root)
# e1.grid(row=0,column=1)
# b=Button(root,text="sqare",command=sqare).grid(row=2,column=3)
# IbRES=Label(root,text="result",bg="yellow").grid(row=3)
# Result=Label(root,textvariable=mytext).grid(row=3,column=1)
#
#
#
#
#
1