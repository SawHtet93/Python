from tkinter import *
myGui = Tk()
def hello():
    b = a.get()
    myLabel2= Label(text= 'User login with: ' + b,fg='black',bg='white').pack()
def dele():
    myLabel3 = Label(text='Delete',fg='black',bg='red').pack()
a = StringVar()   
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='label one',fg='black',bg='red').pack()
myButton1 = Button(text='enter',bg='green',command = hello).pack()
myButton2 = Button(text='Delete',bg='red',font=20,command = dele).pack()

text = Entry(textvariable =a).pack()

myGui.mainloop()
