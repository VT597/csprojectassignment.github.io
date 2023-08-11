import tkinter as tk

def proceed_to_pay():
    # This function will be called when the "Proceed to pay" button is clicked
    pass  # Replace this with your desired functionality

# Create the main window
root = tk.Tk()
root.title("Ticket Booking Page")

# Create widgets
title_label = tk.Label(root, text="UPPER STAND", font=("Helvetica", 16, "bold"))
image_label = tk.Label(root, text="(IMAGE)")
button_us = tk.Button(root, text="BUTTON US")
button_vip = tk.Button(root, text="BUTTON VIP")
button_ls = tk.Button(root, text="BUTTON LS")
choose_row_label = tk.Label(root, text="Choose row:")
button_labels = [tk.Button(root, text=f"BUTTON {chr(65 + i)}") for i in range(8)]
no_of_tickets_label = tk.Label(root, text="No. of tickets:")
input_box = tk.Entry(root)
book_non_continuous_checkbox = tk.Checkbutton(root, text="BOOK NON-CONTINUOUS ST'S")
proceed_button = tk.Button(root, text="Proceed to pay", command=proceed_to_pay)

# Organize widgets using grid layout
title_label.grid(row=0, column=1, columnspan=3)
image_label.grid(row=1, column=0, rowspan=4)
button_us.grid(row=1, column=1)
button_vip.grid(row=2, column=1)
button_ls.grid(row=3, column=1)
choose_row_label.grid(row=1, column=2)
for i, button_label in enumerate(button_labels):
    button_label.grid(row=2 + i // 4, column=2 + i % 4)
no_of_tickets_label.grid(row=6, column=0, sticky=tk.E)
input_box.grid(row=6, column=1)
book_non_continuous_checkbox.grid(row=7, column=1)
proceed_button.grid(row=8, column=1)

# Start the GUI event loop
root.mainloop()
