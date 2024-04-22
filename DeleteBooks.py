#!/usr/bin/env python
# coding: utf-8

# # Delete books Window

# In[4]:


import tkinter as tk
deleteW=tk.Tk()
deleteW.title('Delete Books Window')
deleteW.geometry('550x550')
l1=tk.Label(deleteW,text="Delete Books",font=('Arial',30,'bold'))
l1.grid(row=0,column=1)
l2=tk.Label(deleteW,text="Enter Book id: ",font=('Arial',15,'bold'))
l2.grid(row=1,column=1)
e1=tk.Entry(deleteW)
e1.grid(row=1,column=2)
b1=tk.Button(deleteW,text="Submit",bg="lightblue",font=('Arial',15,'bold'))
b1.grid(row=2,column=1)
deleteW.mainloop()


# In[ ]:




