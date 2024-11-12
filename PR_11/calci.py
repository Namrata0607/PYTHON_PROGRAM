import tkinter as tk
from tkinter import messagebox

# Function to update the input field with the pressed button
def button_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression in the input field
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Main window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field for input and output
entry = tk.Entry(root, font=("Arial", 20), bd=8, insertwidth=2, width=14, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=3, font=("Arial", 14), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button == "C":
        tk.Button(root, text=button, width=5, height=3, font=("Arial", 14), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=5, height=3, font=("Arial", 14), command=lambda x=button: button_click(x)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
