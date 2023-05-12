import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Login Page")
root.resizable(0,0)
root.geometry('1000x562')

back_img=ImageTk.PhotoImage(file="bg1.jpg")

back_lab = tk.Label(root,image=back_img)
back_lab.place(x=0,y=0,relwidth=1,relheight=1)

login_frame = tk.Frame(root, bg="white")
login_frame.pack(expand=True)

username_label = tk.Label(login_frame, text="Username", bg="white", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

username_entry = tk.Entry(login_frame, width=20, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

email_label = tk.Label(login_frame, text="Email", bg="white", font=("Arial", 14))
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

email_entry = tk.Entry(login_frame, width=20, font=("Arial", 14))
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

password_label = tk.Label(login_frame, text="Password", bg="white", font=("Arial", 14))
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="E")

password_entry = tk.Entry(login_frame, show="*", width=20, font=("Arial", 14))
password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

forgot_password_button = tk.Button(login_frame, text="Forgot Password", bg="white", fg="blue", font=("Arial", 12), width=15)
forgot_password_button.grid(row=3, column=0, padx=10, pady=10, sticky="W")

login_button = tk.Button(login_frame, text="Login", bg="blue", fg="white", font=("Arial", 14), width=10, height=1)
login_button.grid(row=3, column=1, padx=10, pady=10, sticky="E")

sign_up_button = tk.Button(root, text="Sign Up", bg="white", fg="blue", font=("Arial", 12), width=10, height=1)
sign_up_button.pack(side="bottom", pady=10, padx=10, anchor="se")

root.mainloop()
