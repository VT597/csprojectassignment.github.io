from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open_file_dialog():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            img = PhotoImage(file=file_path)

            # Resize the image to fit the PFP area (adjust as needed)
            img = img.subsample(2, 2)  # Change the factors (2, 2) to your desired values

            pfp_label.config(image=img)
            pfp_label.image = img  # Keep a reference to avoid garbage collection
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image: {str(e)}")

# Create the main window
profile_window = Tk()
profile_window.title("Profile Page")
profile_window.geometry("800x600")

# Profile Picture (PFP)
pfp_label = Label(profile_window, text="PFP", font=("Arial", 24), relief="solid")
pfp_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

select_pfp_button = Button(profile_window, text="Select PFP", command=open_file_dialog, font=("Arial", 16))
select_pfp_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Username (Retrieve from MySQL or use a placeholder)
username_label = Label(profile_window, text="<USERNAME>", font=("Arial", 24))
username_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Ticket Details
ticket_frame = Frame(profile_window, relief="solid", borderwidth=1)
ticket_frame.grid(row=2, column=0, columnspan=2, pady=20, padx=10, sticky="w")

date_label = Label(ticket_frame, text="<Date>", font=("Arial", 20))
date_label.grid(row=0, column=0, pady=5)

month_label = Label(ticket_frame, text="<Month>           Match 07: SS vs RC", font=("Arial", 20))
month_label.grid(row=1, column=0, pady=5)

year_label = Label(ticket_frame, text="<Year>", font=("Arial", 20))
year_label.grid(row=2, column=0, pady=5)

# Run the Tkinter event loop
profile_window.mainloop()
