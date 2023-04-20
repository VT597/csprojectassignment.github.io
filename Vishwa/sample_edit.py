from tkinter import *
from tkinter import ttk

#creating the window
root=Tk()
frame=ttk.Frame(root,padding=300)
frame.grid()

#login page
Name=Label(frame,text="Username:").grid(column=1,row=1,padx=50)
name_entry=Entry(frame).grid(column=101,row=1,padx=50)
Password=Label(frame,text="Password:").grid(column=1,row=2,rowspan=500,columnspan=100,padx=50,pady=50)
password_entry=Entry(frame).grid(column=101,row=101,padx=50,pady=50)
submit_btn=Button(frame,text="Submit")
submit_btn.place(x=200,y=200)

#running the tkinter code
root.mainloop()

