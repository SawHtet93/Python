from tkinter import *
myGui = Tk()
sec = Tk()
a = StringVar()
def hello():
    b = a.get()
    myLabel2= Label(sec,text= 'User login with: ' + b,fg='black',bg='white').pack()

b = StringVar()
def ss():
    c = b.get()
    myLabel4= Label(text ='User login with: ' + c,fg='black',bg='white').pack()
def dele():
    myLabel3 = Label(sec,text='Delete',fg='black',bg='red').pack()


myGui.geometry("500x500+100+50")
sec.geometry("500x500+100+50")
myLabel1 = Label(text='User One',fg='black',bg='red').pack()
myLabel6 = Label(sec,text='User Two',fg='black',bg='red').pack()

myButton1 = Button(text='enter',bg='green',command = hello).pack()
myButton2 = Button(text='Delete',bg='red',font=20,command = dele).pack()

myButton3 = Button(sec,text='Delete',bg='red',font=20,command = dele).pack()
myButton4 = Button(sec,text='enter',bg='green',command = ss).pack()



text = Entry(textvariable =a).pack()
text2 =Entry(sec,textvariable=b).pack()

myGui.mainloop()
