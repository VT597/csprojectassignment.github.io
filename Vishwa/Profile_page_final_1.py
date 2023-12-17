from tkinter import *
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        pfp_img = PhotoImage(file=file_path)
        pfp_label.config(image=pfp_img)
        pfp_label.image = pfp_img  # Keep a reference to avoid garbage collection

# Create the main window
profile_window = Tk()
profile_window.title("Profile Page")
profile_window.geometry("400x600")

# Profile Picture (PFP)
pfp_label = Label(profile_window, text="PFP", font=("Arial", 16), relief="solid")
pfp_label.pack(pady=10)

select_pfp_button = Button(profile_window, text="Select PFP", command=open_file_dialog)
select_pfp_button.pack(pady=5)

# Username (Retrieve from MySQL or use a placeholder)
username_label = Label(profile_window, text="<USERNAME>", font=("Arial", 14))
username_label.pack(pady=10)

# Ticket Details
ticket_frame = Frame(profile_window, relief="solid", borderwidth=1)
ticket_frame.pack(pady=20, padx=10)

date_label = Label(ticket_frame, text="<Date>", font=("Arial", 12))
date_label.grid(row=0, column=0, pady=5)

month_label = Label(ticket_frame, text="<Month>           Match 07: SS vs RC", font=("Arial", 12))
month_label.grid(row=1, column=0, pady=5)

year_label = Label(ticket_frame, text="<Year>", font=("Arial", 12))
year_label.grid(row=2, column=0, pady=5)

# Run the Tkinter event loop
profile_window.mainloop()
