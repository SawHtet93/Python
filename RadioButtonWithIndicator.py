from tkinter import *
root = Tk()
root.title('radio button')

""" Radiobutton(root,text='radio1',padx=40).pack(anchor=W)
Radiobutton(root,text='radio2',pady=40).pack(anchor=E)
Radiobutton(root,text='radio3',padx=40).pack()
Radiobutton(root,text='radio4',pady=40).pack()  """


v = IntVar()
v.set(3)
"""Label(root,text="Choose a Programming \n Language",padx=25,justify=LEFT).pack(anchor=W)
Radiobutton(root,text="python",padx=25,variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Java",padx=25,variable=v,value=2).pack(anchor=W)
Radiobutton(root,text="C",padx=25,variable=v,value=3).pack(anchor=W)
Radiobutton(root,text="Ruby",padx=25,variable=v,value=4).pack(anchor=W) """


print ("with List \n")

def mmm():
    a = v.get()
    if (a == 1):
        a1 =Tk()
        a1.title('python')
        l1 = Label(a1,text='welcome to python programming').pack()
    elif (a ==2):
        a1= Tk()
        a1.title('Perl')
        l1=Label(a1,text='Welcome to perl Programming').pack()
    elif (a == 3):
        a1= Tk()
        a1.title('C')
        l1=Label(a1,text='Welcome to C Programming').pack()
    else:
        a1= Tk()
        a1.title('Ruby')
        l1=Label(a1,text='Welcome to Ruby Programming').pack()
        

languages = [("python",1),("perl",2),("C",3),("Ruby",4)]
Label(root,text="Choose a programming \n Language",padx=25,justify =LEFT).pack(anchor=W)
for txt,val in languages:
    Radiobutton(root,text=txt,padx=25,variable=v,command=mmm,indicatoron=0,width=25,value=val).pack(anchor=W)

root.mainloop()
