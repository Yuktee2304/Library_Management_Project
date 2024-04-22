#!/usr/bin/env python
# coding: utf-8

# # Add books Window

# In[1]:


import tkinter as tk
from tkinter import messagebox as msg
addW=tk.Tk()
addW.title('Add Books Window')
addW.geometry('440x440')
def add_db():
    global user
    global password
    global host
    global db
    try:
        con=conn.connect(user='root',password='root',host='localhost',db='library_management_project')
        cur=con.cursor()
        id=e1.get()
        title=e2.get()
        author=e3.get()
        sql_query=f'insert into books values({id},{title},{author},{"Yes"})'
        cur.execute(sql_query)
        con.commit()
        msg.showinfo('Success','Books added successfully!!')
    except:
        msg.showerror('Error','Cannot add given book data into Database')
def addBooks():
    l1=tk.Label(addW,text='Add Books',font=('Arial',30,'bold'))
    l1.grid(row=1,column=1)
    l2=tk.Label(addW,text='Enter Book id: ',font=('Arial',15,'bold'))
    l2.grid(row=2,column=1)
    l3=tk.Label(addW,text='Enter Title: ',font=('Arial',15,'bold'))
    l3.grid(row=3,column=1)
    l4=tk.Label(addW,text='Enter Author: ',font=('Arial',15,'bold'))
    l4.grid(row=4,column=1)
    e1=tk.Entry(addW)
    e1.grid(row=2,column=3)
    e2=tk.Entry(addW)
    e2.grid(row=3,column=3)
    e3=tk.Entry(addW)
    e3.grid(row=4,column=3)
    b1=tk.Button(addW,text="Submit",bg="lightblue",font=('Arial',15,'bold'),command=add_db)
    b1.grid(row=6,column=1)
    addW.mainloop()


# In[ ]:




