from tkinter import *
from tkinter import filedialog
a = Tk()

def mfileopen():
    file1 = filedialog.askopenfilename()
    label = Label(text=file1).pack()
    f = open(file1)
    label2 = Label(text=f.read()).pack()
    
button = Button(text='Open File',width=50,command = mfileopen).pack()

