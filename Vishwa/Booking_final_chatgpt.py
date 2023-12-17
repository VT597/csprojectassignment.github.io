from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

# Functions
def uon_enter(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, END)

def pon_enter(event):
    if password_entry.get() == "Password":
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

def forget_pass():
    def change_pass():
        if username_entry.get() == '' or newpass_Entry.get() == '' or confirmpass_Entry.get() == '':
            messagebox.showerror('Error', "All fields need to be entered.", parent=win3)
        elif newpass_Entry.get() != confirmpass_Entry.get():
            messagebox.showerror('Error', "Those passwords didn't match.", parent=win3)
        else:
            con = pymysql.connect(host='localhost', user='root', password='siuu123', database='userdata')
            mycursor1 = con.cursor()
            query = "select * from data where username=%s"
            mycursor1.execute(query, (user_Entry.get(),))
            row = mycursor1.fetchone()
            print(row)
            if row is None:
                messagebox.showerror('Error', "Username doesn't exist. Please check and try again.", parent=win3)
            else:
                query = "update data set password=%s where username=%s"
                mycursor1.execute(query, (newpass_Entry.get(), user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password successfully changed.', parent=win3)
                win3.destroy()

    win3 = Toplevel()
    win3.title('Forgot Password')
    win3.resizable(0, 0)

    bgImage3 = ImageTk.PhotoImage(file='forgotpasswordbg.jpg')
    bgLabel3 = Label(win3, image=bgImage3)
    bgLabel3.grid()

    heading2 = Label(win3, text="RESET PASSWORD", font=('arial', 15, 'bold'), bg='white', fg='Royalblue1')
    heading2.place(x=215, y=85)

    userlabel = Label(win3, text='Username', font=('arial', 10, 'bold'), bg='white', fg='skyblue1')
    userlabel.place(x=205, y=120)

    user_Entry = Entry(win3, width=25, font=("arial", 11, "bold"), fg='royalblue1', bg='white', cursor='tcross', bd=0)
    user_Entry.place(x=205, y=145)

    Frame(win3, width=200, height=2, bg="Skyblue1").place(x=205, y=165)

    password_label = Label(win3, text='New Password', font=('arial', 10, 'bold'), bg='white', fg='skyblue1')
    password_label.place(x=205, y=175)

    newpass_Entry = Entry(win3, width=25, font=("arial", 11, "bold"), fg='royalblue1', bg='white', cursor='tcross',
                          bd=0)
    newpass_Entry.place(x=205, y=200)

    Frame(win3, width=200, height=2, bg="Skyblue1").place(x=205, y=220)

    confirmpassword_label = Label(win3, text='Confirm Password', font=('arial', 10, 'bold'), bg='white',
                                  fg='skyblue1')
    confirmpassword_label.place(x=205, y=230)

    confirmpass_Entry = Entry(win3, width=25, font=("arial", 11, "bold"), fg='royalblue1', bg='white', cursor='tcross',
                              bd=0)
    confirmpass_Entry.place(x=205, y=255)

    Frame(win3, width=200, height=2, bg="Skyblue1").place(x=205, y=275)

    submit_Button = Button(win3, text='Submit', font=("Open Sans", 12, "bold"), fg='White', bg='Royalblue2', bd=0
                           , activebackground='royalblue2', activeforeground='White', width=20, command=change_pass)
    submit_Button.place(x=205, y=300)

    win3.mainloop()

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', "All fields need to be entered.")
    else:
        try:
            con1 = pymysql.connect(host='localhost', user='root', password='siuu123')
            mycursor1 = con1.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not establised. Try again.')
            return

        query = 'use userdata'
        mycursor1.execute(query)
        query = 'select * from  data where username=%s and password=%s'
        mycursor1.execute(query, (username_entry.get(), password_entry.get()))

        row = mycursor1.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Invalid Username or Password. Please check try again.')
        else:
            messagebox.showinfo('Success', 'Successfully Logged In')
            win1.destroy()
            import home

# GUI
win1 = Tk()
win1.geometry('1000x562')
win1.resizable(0, 0)
win1.title("Login Page")
bgImage = ImageTk.PhotoImage(file="bg2.jpg")

bgLabel = Label(win1, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(win1, text="LOGIN PAGE", font=("Lato", 23, "bold"), bg='azure', fg='slate blue')
heading.place(x=600, y=120)

username_entry = Entry(win1, width=25, font=("Lato", 11, "bold"), bd=0, fg='midnight blue', cursor='tcross')
username_entry.place(x=600, y=180)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', uon_enter)

Frame(win1, width=222, height=2, bg="slate blue").place(x=600, y=200)

password_entry = Entry(win1, width=25, font=("Lato", 11, "bold"), bd=0, fg='midnight blue', cursor='tcross')
password_entry.place(x=600, y=240)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', pon_enter)

Frame(win1, width=222, height=2, bg="slate blue").place(x=600, y=260)

openeye = PhotoImage(file="openeye.png")
eyeButton = Button(win1, image=openeye, bd=0, bg='white', activebackground='White', cursor='hand2', command=hide)
eyeButton.place(x=800, y=232)

forgetButton = Button(win1, text="Forgot Password?", bd=0, bg='white', activebackground='White'
                      , cursor='hand2', font=("Lato", 9, "bold"), fg='midnight blue',
                      activeforeground='midnight blue', command=forget_pass)
forgetButton.place(x=715, y=272)

loginButton = Button(win1, text='Login', font=("Open sans", 16, "bold"), fg="White", bg="midnight blue"
                     , cursor='hand2', activebackground='midnight blue', activeforeground='white',
                     bd=0, width=17, command=login_user)
loginButton.place(x=600, y=300)

orLabel = Label(win1, text="--------------OR--------------", font=("Open sans", 16)
                , fg="midnight blue", bg='White')
orLabel.place(x=600, y=345)

singup_Label = Label(win1, text="Don't have an account?", font=("Open sans", 9, 'bold')
                     , fg="midnight blue", bg='White')
singup_Label.place(x=600, y=385)

newaccountButton = Button(win1, text='Create New Account', font=("Open sans", 9, "bold underline")
                          , bg="White", fg="blue2", cursor='hand2', activebackground='white',
                          activeforeground='blue2', bd=0, width=17, command=signup_page)
newaccountButton.place(x=737, y=385)

win1.mainloop()
