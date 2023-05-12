import tkinter as tk
from PIL import ImageTk, Image

# create the root window
root = tk.Tk()
root.title("Login Page")
root.resizable(0, 0)
root.geometry('1000x562')

back_img = ImageTk.PhotoImage(file="bg1.jpg")
back_lab = tk.Label(root, image=back_img)
back_lab.place(x=0, y=0, relwidth=1, relheight=1)

# create a frame for the login form
login_frame = tk.Frame(root, bg=back_lab.cget('background'))
login_frame.pack(expand=True)

# create a label for the username field
username_label = tk.Label(login_frame, text="Username", bg=back_lab.cget('background'), font=("Arial", 20))
username_label.grid(row=0, column=0, padx=20, pady=20, sticky="E")

# create an entry field for the username
username_entry = tk.Entry(login_frame, width=30, font=("Arial", 20))
username_entry.grid(row=0, column=1, padx=20, pady=20, sticky="W")

# create a label for the email field
email_label = tk.Label(login_frame, text="Email", bg=back_lab.cget('background'), font=("Arial", 20))
email_label.grid(row=1, column=0, padx=20, pady=20, sticky="E")

# create an entry field for the email
email_entry = tk.Entry(login_frame, width=30, font=("Arial", 20))
email_entry.grid(row=1, column=1, padx=20, pady=20, sticky="W")

# create a label for the password field
password_label = tk.Label(login_frame, text="Password", bg=back_lab.cget('background'), font=("Arial", 20))
password_label.grid(row=2, column=0, padx=20, pady=20, sticky="E")

# create an entry field for the password
password_entry = tk.Entry(login_frame, show="*", width=30, font=("Arial", 20))
password_entry.grid(row=2, column=1, padx=20, pady=20, sticky="W")

# create a forgot password button
forgot_password_button = tk.Button(login_frame, text="Forgot Password", bg=back_lab.cget('background'), fg="blue", font=("Arial", 16), width=15)
forgot_password_button.grid(row=3, column=0, padx=20, pady=20, sticky="W")

# create a login button
login_button = tk.Button(login_frame, text="Login", bg="blue", fg="white", font=("Arial", 20), width=15, height=2)
login_button.grid(row=3, column=1, padx=20, pady=20, sticky="E")

# create a sign up button
sign_up_button = tk.Button(root, text="Sign Up", bg=back_lab.cget('background'), fg="blue", font=("Arial", 16), width=10, height=1)
sign_up_button.pack(side="bottom", pady=20, padx=20, anchor="se")

# run the main event loop
root.mainloop()
