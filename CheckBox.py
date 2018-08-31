from tkinter import *

def mget():
    print (var1.get(),var2.get(),var3.get(),var4.get())
a =Tk()
var1 = IntVar()
Checkbutton(a,text="checkbutton1",variable=var1).grid(row=0,stick=W)
var2=IntVar()
Checkbutton(a,text="Checkbutton2",variable=var2).grid(row=1,stick=W)
var3=IntVar()
Checkbutton(a,text="checkbutton3",variable=var3).grid(row=2,stick=W)
var4=IntVar()
Checkbutton(a,text="Checkbutton4",variable=var4).grid(row=3,stick=W)

Button(a,text="Get Value",command = mget,width =15).grid(row=4,stick=W)
Button(a,text="Qucik",command =a.destroy,width =25).grid(row=5,stick=W)

a.mainloop()
