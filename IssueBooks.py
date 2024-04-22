#!/usr/bin/env python
# coding: utf-8

# # Issue Books Window

# In[3]:


import tkinter as tk
issueW=tk.Tk()
issueW.title('Issue Books Window')
issueW.geometry('550x550')
l1=tk.Label(issueW,text="Issue Books",font=('Arial',30,'bold'))
l1.grid(row=0,column=1)
l2=tk.Label(issueW,text="Enter Book id: ",font=('Arial',15,'bold'))
l2.grid(row=1,column=1)
l3=tk.Label(issueW,text="Enter Student Name: ",font=('Arial',15,'bold'))
l3.grid(row=2,column=1)
e1=tk.Entry(issueW)
e1.grid(row=1,column=3)
e2=tk.Entry(issueW)
e2.grid(row=2,column=3)
b1=tk.Button(issueW,text="Submit",font=('Arial',15,'bold'),bg="lightblue")
b1.grid(row=3,column=1)
issueW.mainloop()


# In[ ]:




