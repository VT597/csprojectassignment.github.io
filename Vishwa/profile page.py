import tkinter as tk
import sqlite3
from tkinter import ttk

def edit_profile():
    # This function will be called when the edit (pencil) icon is clicked
    # Implement profile editing logic here
    pass

def update_profile():
    # This function will be called when the "Update" button is clicked after editing
    # Implement profile update logic here
    pass

def load_profile():
    # This function will load user profile details from the database
    # Implement profile loading logic here
    pass

# Create the main window
root = tk.Tk()
root.title("Profile Page")

# Create a database or connect to an existing one
conn = sqlite3.connect("profile.db")
cursor = conn.cursor()

# Create the profile table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY,
    username TEXT,
    address TEXT,
    email TEXT,
    booked_tickets TEXT
)''')
conn.commit()

# Load profile data from the database (for demonstration purposes)
profile_data = {"username": "John Doe", "address": "123 Main St", "email": "john@example.com", "booked_tickets": "Match 1, Match 2"}

# Create labels and entry fields for profile details
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)
username_entry.insert(0, profile_data["username"])

address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)
address_entry.insert(0, profile_data["address"])

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
email_entry.insert(0, profile_data["email"])

# Create "Edit" button and "Update" button
edit_button = tk.Button(root, text="Edit", command=edit_profile)
update_button = tk.Button(root, text="Update", command=update_profile)

# Place widgets on the window
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

address_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
address_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

edit_button.grid(row=3, column=0, padx=10, pady=10)
update_button.grid(row=3, column=1, padx=10, pady=10)

# Load and display booked ticket history
ticket_history_label = tk.Label(root, text="Booked Ticket History:")
ticket_history_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

# Load and display booked ticket history from the database (for demonstration purposes)
booked_tickets = profile_data["booked_tickets"].split(", ")
for i, ticket in enumerate(booked_tickets):
    ticket_label = tk.Label(root, text=f"{i + 1}. {ticket}")
    ticket_label.grid(row=5 + i, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Start the GUI event loop
root.mainloop()
