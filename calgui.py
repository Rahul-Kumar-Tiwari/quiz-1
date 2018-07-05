#calculator

import tkinter
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Calculator")
root.geometry("350x360")
root.resizable(True,True)
root.minsize(200,200)
#root.maxsize(300,300)

l1 = ttk.Label(root,text="Test").pack()

entry=Entry(root,width=56,bd=5,bg='beige',justify='right',validatecommand = vcmd)
entry.pack()
f1=Frame(root)
f1.pack()

#ttk.Button(f1)
b1=Button(f1,text='7',bd=2,width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f1,text='8',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f1,text='9',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f1,text='+',width=10,height=5)
b1.pack(side=LEFT)

f2=Frame(root)
f2.pack()

b1=Button(f2,text='4',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f2,text='5',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f2,text='6',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f2,text='-',width=10,height=5)
b1.pack(side=LEFT)

f3=Frame(root)
f3.pack()

b1=Button(f3,text='1',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f3,text='2',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f3,text='3',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f3,text='*',width=10,height=5)
b1.pack(side=LEFT)

f4=Frame(root)
f4.pack()

b1=Button(f4,text='0',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f4,text='.',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f4,text='/',width=10,height=5)
b1.pack(side=LEFT)
b1=Button(f4,text='=',width=10,height=5)
b1.pack(side=LEFT)

root.mainloop()