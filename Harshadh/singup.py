from tkinter import *
from PIL import ImageTk

def login_page():
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

confirmpassword_Entry= Entry(frame, width=35, font=("Lato",11,"bold"),fg='White',bg='slate blue',cursor='tcross')
confirmpassword_Entry.grid(row=8,column=0,sticky='w', padx=30)

tac= Checkbutton(frame,text= "I agree to the Terms & Conditions", font=("Lato",10,"bold")
                 ,fg='slate blue',bg='White',bd=0,activeforeground='slate blue'
                 ,activebackground='White',cursor='hand2')
tac.grid(row=9,column=0,sticky='w',padx= 15,pady=2)

signup_Button= Button(frame, text='Sign Up', font=("Open Sans",16,"bold"),fg='White',bg='slate blue',bd=0
                      ,activebackground= 'slate blue',activeforeground='White',width=20)
signup_Button.grid(row=10,column=0,pady=5)

alreadyaccount_Label= Label(frame, text='Already have an account?', font=("Lato",9,"bold"),
                            bg='White',fg='slate blue')
alreadyaccount_Label.grid(row=11,column=0,sticky='w',padx=30)

login_Button= Button(win2, text= 'Log In',font=("Open sans",9,"bold underline")
                         ,bg= "White", fg="blue2" ,cursor='hand2' ,activebackground= 'white',
                         activeforeground='blue2',bd=0,command=login_page)
login_Button.place(x=700,y=420)

win2.mainloop()
