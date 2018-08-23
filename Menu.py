from tkinter import *
myGui = Tk()
myGui.geometry("500x500+100+50")

myButton1 = Button(text='Click Me',bg='green',fg='white').pack()

mymenu = Menu()
mymenu.add_cascade(label='File')
mymenu.add_cascade(label='Edit')
mymenu.add_cascade(label='Help')
mymenu.add_cascade(label='About')

myGui.config(menu=mymenu)




myGui.mainloop()
