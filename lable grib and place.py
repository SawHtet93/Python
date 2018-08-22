from tkinter import *
myGui = Tk()
myGui.title("Size and Position")
myGui.geometry("500x500+0+0")
myLabel1 = Label(text='Label one',fg='red',bg='black').pack()
#.pack() for colour and label
myLabel2 = Label(text='Label Two',fg='red',bg='black') #class
myLabel2.pack()  #Method
myLabel3 = Label(text='Label Three',fg='red',bg='black').place(x=0,y=100)

#myLabel4 = Label(text='Label Four',fg='red',bg='black').grid(row=0,column=0,sticky='w')

myGui.mainloop() 
