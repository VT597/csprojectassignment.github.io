from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def login_page():
    win2.destroy()
    import signin

def clear():
    email_Entry.delete(0,END)
    username_Entry.delete(0,END)
    password_Entry.delete(0,END)
    con2firmpassword_Entry.delete(0,END)
    checktac.set(0)

def con2nect_database():
    if email_Entry.get()=="" or username_Entry.get()=="" or password_Entry.get()=='' or con2firmpassword_Entry.get()=="":
        messagebox.showerror('Error','All fields need to be entered.')
    elif password_Entry.get()!=con2firmpassword_Entry.get():
        messagebox.showerror('Error', 'Those passwords didn’t match. Try again.')
    elif checktac.get()==0:
        messagebox.showerror('Error', 'Please agree to our Terms & con2ditions.')
    else:
        try:
            con2=pymysql.con2nect(host='<Your Host>', user='<Your user>', password='<Your Password>')
            mycursor2= con2.cursor()
        except:
            messagebox.showerror('Error', 'Database con2nectivity issue. Please try again.')
            return
        try:
            query= 'create database userdata'
            mycursor2.execute(query)
            query= 'use userdata'
            mycursor2.execute(query)
            query= 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(25))'
            mycursor2.execute(query)
        except:
            mycursor2.execute('use userdata')
        query= 'select * from data where username=%s'
        mycursor2.execute(query,(username_Entry.get()))

        row= mycursor2.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'Username already exists')
        else:
            query= 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor2.execute(query,(email_Entry.get(),username_Entry.get(),password_Entry.get()))
            con2.commit()
            con2.close()
            messagebox.showinfo('Success', 'Successfully registered.')
            clear()
            win2.destroy()
            import signin

win2= Tk()
win2.geometry('1000x562')
win2.resizable(0,0)
win2.title("Sign Up Page")
bgImage2= ImageTk.PhotoImage(file='bg2.jpg')

bgLabel= Label(win2, image=bgImage2)
bgLabel.grid()

frame= Frame(win2,bg='White')
frame.place(x=522,y=113)

heading= Label(frame,text="CREATE AN ACCOUNT", font=("Lato",22,"bold"),bg='white',fg='slate blue')
heading.grid(row= 0, column= 0,padx=10,pady=1)

email_Label= Label(frame, text='Email', font=("Lato",11,"bold"),bg='White',fg='slate blue')
email_Label.grid(row=1,column=0,sticky='w',padx=30,pady=(2,0))

email_Entry= Entry(frame, width=35, font=("Lato",11,"bold"),fg='White',bg='slate blue',cursor='tcross')
email_Entry.grid(row=2,column=0,sticky='w', padx=30)

username_Label= Label(frame, text='Username', font=("Lato",11,"bold"),bg='White',fg='slate blue')
username_Label.grid(row=3,column=0,sticky='w',padx=30,pady=(2,0))

username_Entry= Entry(frame, width=35, font=("Lato",11,"bold"),fg='White',bg='slate blue',cursor='tcross')
username_Entry.grid(row=4,column=0,sticky='w', padx=30)

password_Label= Label(frame, text='Password', font=("Lato",11,"bold"),bg='White',fg='slate blue')
password_Label.grid(row=5,column=0,sticky='w',padx=30,pady=(2,0))

password_Entry= Entry(frame, width=35, font=("Lato",11,"bold"),fg='White',bg='slate blue',cursor='tcross')
password_Entry.grid(row=6,column=0,sticky='w', padx=30)

confirmpassword_Label= Label(frame, text='Confirm Password', font=("Lato",11,"bold"),bg='White',fg='slate blue')
confirmpassword_Label.grid(row=7,column=0,sticky='w',padx=30,pady=(2,0))

con2firmpassword_Entry= Entry(frame, width=35, font=("Lato",11,"bold"),fg='White',bg='slate blue',cursor='tcross')
con2firmpassword_Entry.grid(row=8,column=0,sticky='w', padx=30)

checktac= IntVar()
tac= Checkbutton(frame,text= "I agree to the Terms & con2ditions", font=("Lato",10,"bold")
                 ,fg='slate blue',bg='White',bd=0,activeforeground='slate blue'
                 ,activebackground='White',cursor='hand2',variable=checktac)
tac.grid(row=9,column=0,sticky='w',padx= 15,pady=2)

signup_Button= Button(frame, text='Sign Up', font=("Open Sans",16,"bold"),fg='White',bg='slate blue',bd=0
                      ,activebackground= 'slate blue',activeforeground='White',width=20,command=con2nect_database)
signup_Button.grid(row=10,column=0,pady=5)

alreadyaccount_Label= Label(frame, text='Already have an account?', font=("Lato",9,"bold"),
                            bg='White',fg='slate blue')
alreadyaccount_Label.grid(row=11,column=0,sticky='w',padx=30)

login_Button= Button(win2, text= 'Log In',font=("Open sans",9,"bold underline")
                         ,bg= "White", fg="blue2" ,cursor='hand2' ,activebackground= 'white',
                         activeforeground='blue2',bd=0,command=login_page)
login_Button.place(x=700,y=420)

win2.mainloop()
