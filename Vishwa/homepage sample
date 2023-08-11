import tkinter as tk

def open_about_us():
    # This function will be called when the "About us" button is clicked
    # You can implement the logic to navigate to the About Us page here
    pass

def open_book_tickets():
    # This function will be called when the "Book Tickets" button is clicked
    # You can implement the logic to navigate to the Book Tickets page here
    pass

# Create the main window
root = tk.Tk()
root.title("Homepage")

# Create widgets
home_label = tk.Label(root, text="Home", font=("Helvetica", 16, "bold"))
about_us_button = tk.Button(root, text="About us", command=open_about_us)
book_tickets_button = tk.Button(root, text="Book Tickets", command=open_book_tickets)
about_ssfc_label = tk.Label(root, text="About SS FC", font=("Helvetica", 14, "bold"))
description_label = tk.Label(root, text="A club like no other, SS FC has been one of the best clubs in the country ever")

# Organize widgets using grid layout
home_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
about_us_button.grid(row=0, column=1, padx=10, pady=10)
book_tickets_button.grid(row=0, column=2, padx=10, pady=10)
about_ssfc_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
description_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
