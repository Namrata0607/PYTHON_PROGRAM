import tkinter as tk
from tkinter import messagebox
import re

def register():
    # Retrieve input values
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get().strip()
    age = entry_age.get().strip()

    # Name validation (only letters and spaces, minimum length 2)
    if not re.match(r"^[A-Za-z\s]{2,}$", name):
        messagebox.showerror("Error", "Name must contain only letters and spaces, with a minimum of 2 characters.")
        return

    # Email validation
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Invalid email format.")
        return

    # Password validation
    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    # Age validation
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "Age must be a positive number.")
        return

    # Success message
    messagebox.showinfo("Success", "Registration successful!")

# Creating the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x350")
root.configure(bg="#f2f2f2")

# Styling for labels and entries
label_font = ("Arial", 12)
entry_font = ("Arial", 11)

# Header
header = tk.Label(root, text="User Registration Form", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333")
header.pack(pady=10)

# Frame for form fields
form_frame = tk.Frame(root, bg="#f2f2f2")
form_frame.pack(pady=10)

# Name label and entry
label_name = tk.Label(form_frame, text="Name:", font=label_font, bg="#f2f2f2")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(form_frame, font=entry_font)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Email label and entry
label_email = tk.Label(form_frame, text="Email:", font=label_font, bg="#f2f2f2")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(form_frame, font=entry_font)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Password label and entry
label_password = tk.Label(form_frame, text="Password:", font=label_font, bg="#f2f2f2")
label_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_password = tk.Entry(form_frame, show="*", font=entry_font)
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Age label and entry
label_age = tk.Label(form_frame, text="Age:", font=label_font, bg="#f2f2f2")
label_age.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_age = tk.Entry(form_frame, font=entry_font)
entry_age.grid(row=3, column=1, padx=10, pady=10)

# Register button
register_button = tk.Button(root, text="Register", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=register)
register_button.pack(pady=20, ipadx=10, ipady=5)

root.mainloop()
