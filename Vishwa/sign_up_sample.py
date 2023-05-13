import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Sign Up Page")
root.resizable(0,0)
root.geometry('1000x562')

back_img=ImageTk.PhotoImage(file="bg1.jpg")
back_lab = tk.Label(root,image=back_img)
back_lab.place(x=0,y=0,relwidth=1,relheight=1)

signup_frame = tk.Frame(root, bg="white")
signup_frame.pack(expand=True)

username_label = tk.Label(signup_frame, text="Username", bg="white", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

username_entry = tk.Entry(signup_frame, width=20, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

email_label = tk.Label(signup_frame, text="Email", bg="white", font=("Arial", 14))
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

email_entry = tk.Entry(signup_frame, width=20, font=("Arial", 14))
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

password_label = tk.Label(signup_frame, text="Password", bg="white", font=("Arial", 14))
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="E")

password_entry = tk.Entry(signup_frame, show="*", width=20, font=("Arial", 14))
password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

signup_button = tk.Button(signup_frame, text="Sign Up", bg="blue", fg="white", font=("Arial", 14), width=10, height=1)
signup_button.grid(row=3, column=1, padx=10, pady=10, sticky="E")

root.mainloop()
