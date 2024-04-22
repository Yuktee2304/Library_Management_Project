#!/usr/bin/env python
# coding: utf-8

# # Return Books Window

# In[8]:


import tkinter as tk
returnW=tk.Tk()
returnW.title('Return Books Window')
returnW.geometry('550x550')
l1=tk.Label(returnW,text="Return Books",font=('Arial',30,'bold'))
l1.grid(row=0,column=1)
l2=tk.Label(returnW,text="Enter Book id: ",font=('Arial',15,'bold'))
l2.grid(row=1,column=1)
e1=tk.Entry(returnW)
e1.grid(row=1,column=2)
b1=tk.Button(returnW,text="Submit",font=('Arial',15,'bold'),bg='lightblue')
b1.grid(row=2,column=1)
returnW.mainloop()


# In[ ]:




