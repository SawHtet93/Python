from tkinter import *
myGui = Tk()
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='label one',fg='red',bg='green').pack()
myButton1 = Button(text='enter',bg='green').pack()
myButton2 = Button(text='Delete',bg='red').pack()

myGui.mainloop()
