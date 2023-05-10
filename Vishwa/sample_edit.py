import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Set the window size dynamically based on device configuration
width = root.winfo_screenwidth() * 0.5
height = root.winfo_screenheight() * 0.5
root.geometry("%dx%d+0+0" % (width, height))

# Load the background image
# TODO: Paste the background image in the project directory and load it here
background_image = tk.PhotoImage(file="Homepage.jpg")

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load the logo image
# TODO: Paste the logo image in the project directory and load it here
logo_image = tk.PhotoImage(file="Homepage.jpg")

# Create a label to display the logo image
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

# Create a frame for the login form
login_frame = tk.Frame(root, bg="white", padx=50, pady=50)
login_frame.pack(side="right", fill="both", expand=True)

# Create a label for the username field
username_label = tk.Label(login_frame, text="Username", bg="white")
username_label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field for the username
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label for the email field
email_label = tk.Label(login_frame, text="Email", bg="white")
email_label.grid(row=1, column=0, padx=10, pady=10)

# Create an entry field for the email
email_entry = tk.Entry(login_frame)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label for the password field
password_label = tk.Label(login_frame, text="Password", bg="white")
password_label.grid(row=2, column=0, padx=10, pady=10)

# Create an entry field for the password
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a login button
login_button = tk.Button(login_frame, text="Login", bg="blue", fg="white", padx=10, pady=10)
login_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Create a forgot password button
forgot_button = tk.Button(login_frame, text="Forgot Password", bg="white", fg="blue", padx=10, pady=10)
forgot_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Create a sign up button
signup_button = tk.Button(root, text="Sign Up", bg="white", fg="blue")
signup_button.pack(side="left", padx=50, pady=50)

# Start the main event loop
root.mainloop()
