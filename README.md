# PSWRDGNTR
from password_generator import PasswordGenerator
password=PasswordGenerator()
password.minlen=6
password.maxlen=8
password.minuchars=2
password.minlchars=2
password.maxschars=0
password.minnumbers=2
def create():
    result=password.generate()
    pw.insert(0,result)
0
def delete1():
    pw.delete(0,END)
from tkinter import *
master=Tk()
delete1
label1=Label(master,text='Password Generator')
pw=Entry(master)
Generate=Button(master,text='Generate',command=create)
clear=Button(master,text='clear',command=delete1)
label1.grid(row=0,column=0)
pw.grid(row=1,column=0)
Generate.grid(row=2,column=0)
clear.grid(row=3,column=0)
master.mainloop()
