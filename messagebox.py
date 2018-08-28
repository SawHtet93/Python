from tkinter import *
from tkinter import messagebox
myGui = Tk()
myGui.geometry("500x500+100+50")

def mbox():
    messagebox.showinfo("Message Box", "This is the first time message box testing")
    

myLabel1 = Label(myGui,text='This is the message box testing\n',fg='green',font=20).pack()

myButton1 = Button(myGui,text='Click to show message box',fg='red',bg='white',command=mbox).pack()
