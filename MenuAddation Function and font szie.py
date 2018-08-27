from tkinter import *
myGui = Tk()

def cl():
    clLabel = Label(text='User click:').pack()

def newfi():
    fileLabel = Label(text='Click on new file',fg='yellow',bg='pink',font=('arial',12,'italic')).pack()

def ab():
    about = Label(text='This is the testing program for menu and list',fg='black',bg='white',font=('arial',16,'italic')).pack()

myGui.geometry("500x500+100+50")
myLabel1 = Label(text='label one',fg='black',bg='red').pack()
myButton1 =Button(text='cleck here',bg='green',command = cl).pack()

mymenu = Menu()
listone = Menu()
listone.add_command(label='New File',command = newfi)
listone.add_command(label='Edit')

listwo = Menu()
listwo.add_command(label='Help')


mymenu.add_cascade(label='File',menu=listone)
mymenu.add_cascade(label='Edit',menu=listone)
mymenu.add_cascade(label='Help',menu=listwo)
mymenu.add_cascade(label='About',command = ab)

myGui.config(menu=mymenu)

myGui.mainloop()
