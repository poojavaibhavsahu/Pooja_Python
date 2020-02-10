from tkinter import*
root=Tk()

root.title("ragistrationform")
root.geometry("500x500")
title=Label(root,text="ragistration form",width=20,font=("bold",20))
title.place(x=90,y=53)
firstname=Label(root,text="fullname",width=20,font=("bold",10))
firstname.place(x=80,y=130)

e1=Entry(root)
e1.place(x=240,y=130)

Email=Label(root,text="Email",width=20,font=("bold",10))
Email.place(x=68,y=180)

e2=Entry(root)
e2.place(x=240,y=180)


gender=Label(root,text="gender",width=20,font=("bold",10))
gender.place(x=78,y=230)


var=IntVar()
Radiobutton(root,text="male",variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="femail",variable=var,value=2).place(x=295,y=230)


country=Label(root,text="country",width=20,font=("bold",10))
country.place(x=78,y=280)

List1=['canada','iceland','india']
c=StringVar()
droplist=OptionMenu(root,c,*List1)
c.set('select your country')
droplist.place(x=240,y=280)

programming=Label(root,text="programming",width=20,font=("bold",10))
programming.place(x=85,y=330)

var1=IntVar()
Checkbutton(root,text="python",variable=var1).place(x=235,y=330)


var2=IntVar()
Checkbutton(root,text="java",variable=var2).place(x=290,y=330)

Button(root,text="submit",width=20,bg="brown",fg="white").place(x=180,y=380)




root.mainloop()















# #var=IntVar()
# n1=Label(root,text="fullname").grid(row=0)
# n2=Label(root,text="email").grid(row=1)
# n3=Label(root,text="gender").grid(row=2)
# n4=Label(root,text="country")
# n5=Label(root,text="programming")
# # Radiobutton(root,text="male",variable=var,value=1).grid(row=0)
# # Radiobutton(root,text='female',variable=var,value=2).grid()
# var1=IntVar()
# Checkbutton(root,text='java',variable=var1).grid(row=0)
# var2=IntVar()
# Checkbutton(root,text="python",variable=var2).grid(row=0)
# Button(root,text="submit").pack()
#
# root.mainloop()