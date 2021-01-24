#!/usr/bin/env python
# coding: utf-8

# In[1]:


from password_generator import PasswordGenerator


# In[2]:


password=PasswordGenerator()


# In[3]:


password.minlen=6
password.maxlen=8
password.minuchars=2
password.minlchars=2
password.maxschars=0
password.minnumbers=2


# In[4]:


def create():
    result=password.generate()
    pw.insert(0,result)


# In[5]:


def delete1():
    pw.delete(0,END)


# In[6]:


from tkinter import *


# In[7]:


master=Tk()


# In[8]:


label1=Label(master,text='Password Generator')
pw=Entry(master)
Generate=Button(master,text='Generate',command=create)
clear=Button(master,text='clear',command=delete1)


# In[9]:


label1.grid(row=0,column=0)
pw.grid(row=1,column=0)
Generate.grid(row=2,column=0)
clear.grid(row=3,column=0)


# In[ ]:


master.mainloop()


# In[ ]:




