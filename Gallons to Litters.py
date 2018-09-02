from tkinter import *
a = Tk()
var1 = IntVar()
n = "arial",14,"bold"
def mcal():
    var2 = var1.get()
    var3 = var2 * 3.785
    e2.insert(0,var3)
def mclear():
    e1.delete(0,END)
    e2.delete(0,END)

Label(a,text='Gallons',padx=25,font=(n)).grid(row=0,sticky=W)
Label(a,text='Litres',padx=25,font=(n)).grid(row=1,sticky=W)

e1=Entry(a,width=25,textvariable=var1)   #textvariable for default variable
e1.grid(row=0,column=1)

e2=Entry(a)
e2.grid(row=1,column=1)


Button(a,text='Calculate G and Lit',command = mcal).grid(row=2,column=1)
Button(a,text='Clear',command = mclear).grid(row=2,column=2)
Button(a,text='Exit',command =a.destroy).grid(row=3,column=1)


a.mainloop()
