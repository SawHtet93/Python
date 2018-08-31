from tkinter import *
root = Tk()
root.title('radio button')

Radiobutton(root,text='radio1',padx=40).pack(anchor=W)
Radiobutton(root,text='radio2',padx=40).pack(anchor=E)
Radiobutton(root,text='radio3',padx=40).pack()
Radiobutton(root,text='radio4',padx=40).pack()

root.mainloop()
