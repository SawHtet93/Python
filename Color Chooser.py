from tkinter import *
from tkinter import colorchooser
a = Tk()

def mcolor():
        color = colorchooser.askcolor()
        label = Label(text='your choosed color \n',bg=color[1]).pack()
      
button = Button(text='choose color',width = 30,command = mcolor).pack()
