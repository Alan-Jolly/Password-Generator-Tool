import random
import string
import pyperclip  # For clipboard functionality
import tkinter as tk
from tkinter import messagebox

# Password Generator Function
def generate_password():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choices(characters, k=length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Copy to Clipboard Function
def copy_to_clipboard():
    pyperclip.copy(result_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# UI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w')

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
result_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

root.mainloop()
