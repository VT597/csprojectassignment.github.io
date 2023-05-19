from tkinter import *
from PIL import ImageTk

#Functions
def uon_enter(event):
    if username_entry.get()=="Username":
        username_entry.delete(0, END)

def pon_enter(event):
    if password_entry.get()=="Password":
        password_entry.delete(0, END)

def hide():
    openeye.config(file="eye.png")
    password_entry.config(show="*")
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password_entry.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    win1.destroy()
    import signup

#GUI
win1= Tk()
win1.geometry('1000x562')
win1.resizable(0,0)
win1.title("Login Page")
bgImage= ImageTk.PhotoImage(file="bg2.jpg")

bgLabel= Label(win1, image=bgImage)
bgLabel.place(x=0,y=0)

heading= Label(win1,text="LOGIN PAGE", font=("Lato",23,"bold"),bg='azure',fg='slate blue')
heading.place(x=600,y=120)

username_entry= Entry(win1,width=25, font=("Lato",11,"bold"),bd=0,fg='midnight blue',cursor='tcross')
username_entry.place(x=600, y= 180)
username_entry.insert(0,'Username')
username_entry.bind('<FocusIn>',uon_enter)

Frame(win1,width=222,height=2,bg="slate blue").place(x=600,y=200)

password_entry= Entry(win1,width=25, font=("Lato",11,"bold"),bd=0,fg='midnight blue',cursor='tcross')
password_entry.place(x=600, y= 240)
password_entry.insert(0,'Password')
password_entry.bind('<FocusIn>',pon_enter)

Frame(win1,width=222,height=2,bg="slate blue").place(x=600,y=260)

openeye= PhotoImage(file="openeye.png")
eyeButton= Button(win1,image= openeye,bd=0,bg='white',activebackground='White',cursor='hand2',command=hide)
eyeButton.place(x=800,y=232)

forgetButton= Button(win1,text= "Forgot Password?",bd=0,bg='white',activebackground='White'
                     ,cursor='hand2', font=("Lato",9,"bold"),fg='midnight blue',
                     activeforeground='midnight blue')
forgetButton.place(x=715,y=272)

loginButton= Button(win1, text= 'Login',font=("Open sans",16,"bold"), fg= "White", bg="midnight blue"
                    ,cursor='hand2' ,activebackground= 'midnight blue', activeforeground='white',
                    bd=0,width=17)
loginButton.place(x=600,y=300)

orLabel= Label(win1,text="--------------OR--------------",font=("Open sans",16)
               ,fg= "midnight blue",bg='White')
orLabel.place(x=600,y=345)

singup_Label= Label(win1,text="Don't have an account?",font=("Open sans",9,'bold')
               ,fg= "midnight blue",bg='White')
singup_Label.place(x=600,y=385)

newaccountButton= Button(win1, text= 'Create New Account',font=("Open sans",9,"bold underline")
                         ,bg= "White", fg="blue2" ,cursor='hand2' ,activebackground= 'white',
                         activeforeground='blue2',bd=0,width=17,command=signup_page)
newaccountButton.place(x=737,y=385)

win1.mainloop()
