import tkinter as tk
from tkinter import filedialog
from customtkinter import *

# Create the main window
root = CTk()  # Use CTk for a custom look
root.geometry("300x150")  # Set the initial window size

# Create label variables to hold the directory paths (define them first!)
directory_label1 = tk.Label(root, text="")  # Initialize with empty text
directory_label2 = tk.Label(root, text="")


# Function to handle directory selection (now takes a label argument)
def select_directory(label):
    directory = filedialog.askdirectory()
    label.config(text=directory)


# Create buttons and pack the labels
directory_label1.pack()
select_button1 = tk.Button(
    root, text="Select", command=lambda: select_directory(directory_label1)
)
select_button1.pack()

directory_label2.pack()
select_button2 = tk.Button(
    root, text="Select", command=lambda: select_directory(directory_label2)
)
select_button2.pack()

# Add a confirm button
confirm_button = tk.Button(root, text="Confirm", command=root.destroy)
confirm_button.pack()

# Run the main loop
root.mainloop()
