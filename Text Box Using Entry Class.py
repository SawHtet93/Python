from tkinter import *
a = Tk()

def fordel():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


Label(a,text='First Name').grid(row=0)
Label(a,text='Last Name').grid(row=1)
Label(a,text='Email ').grid(row=2)
Label(a,text='Country').grid(row=3)



e1 =Entry(a)
e1.grid(row=0,column=1)
e1.insert(0,"Saw")
e2=Entry(a)
e2.grid(row=1,column=1)
e2.insert(0,"Htet")   #insert for default value   
e3=Entry(a)
e3.grid(row=2,column=1)
e3.insert(0,"test@gmail.com")
e4=Entry(a)
e4.grid(row=3,column=1)
e4.insert(0,"Myanmar")



button1= Button(a,text='Clear',command = fordel).grid(row=4,column=1)


a.mainloop()

