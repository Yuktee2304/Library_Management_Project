#!/usr/bin/env python
# coding: utf-8

# # MYSQL Project-2
# ## We are going to build an advanced python project Library Management System using MySQL database and Tkinter for GUI (Graphical User interface).
# 
# ## Tkinter is Python’s standard GUI interface and it is easy to learn. Even if you don’t know anything about tkinter you can just learn it along with this project, we have used some basic widgets like Button, Label, and Entry, etc.
# 
# # This is Home page

# In[1]:


pip install tkinter


# In[2]:


pip install mysql-python-connector as conn


# In[ ]:


import tkinter as tk
import mysql.connector

from library_management_project.AddBooks import *
from library_management_project.ReturnBooks import *
from library_management_project.IssueBooks import *
from library_management_project.ViewBooks import *
from library_management_project.DeleteBooks import *

main=tk.Tk()
main.title('Library Management Project')
main.geometry('850x550')
l1=tk.Label(main,text="Welcome to Library Management System!!",font=('Arial',30,'bold'))
l1.grid(row=1,columnspan=3)
addBtn=tk.Button(main,text="Add Books",font=('Arial',15),background='lightblue',borderwidth=5,command=addBooks)
addBtn.grid(row=3,columnspan=3)
deleteBtn=tk.Button(main,text="Delete Books",font=('Arial',15),background='lightblue',borderwidth=5)
deleteBtn.grid(row=4,columnspan=3)
issueBtn=tk.Button(main,text="Issue Books",font=('Arial',15),background='lightblue',borderwidth=5)
issueBtn.grid(row=5,columnspan=3)
returnBtn=tk.Button(main,text="Return Books",font=('Arial',15),background='lightblue',borderwidth=5)
returnBtn.grid(row=6,columnspan=3)
viewBtn=tk.Button(main,text="View Books",font=('Arial',15),background='lightblue',borderwidth=5)
viewBtn.grid(row=7,columnspan=3)
l2=tk.Label(main,text="Thank you",font=('Arial',15,'bold'))
l2.grid(row=8,columnspan=3)
main.mainloop()


# In[ ]:




