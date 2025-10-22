import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())

    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# --- GUI Setup ---
window = tk.Tk()
window.title("🔐 Password Generator")
window.geometry("400x350")
window.config(bg="#222")

# Title Label
tk.Label(window, text="Advanced Password Generator", font=("Arial", 14, "bold"), bg="#222", fg="white").pack(pady=10)

# Password length
tk.Label(window, text="Enter password length:", bg="#222", fg="white").pack()
length_entry = tk.Entry(window, width=10, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Checkboxes for character types
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=uppercase_var, bg="#222", fg="white").pack(anchor="w", padx=40)
tk.Checkbutton(window, text="Include Lowercase (a-z)", variable=lowercase_var, bg="#222", fg="white").pack(anchor="w", padx=40)
tk.Checkbutton(window, text="Include Digits (0-9)", variable=digits_var, bg="#222", fg="white").pack(anchor="w", padx=40)
tk.Checkbutton(window, text="Include Symbols (!@#$%)", variable=symbols_var, bg="#222", fg="white").pack(anchor="w", padx=40)

# Generate button
tk.Button(window, text="Generate Password", command=generate_password, bg="#00b894", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=10)

# Password display box
password_entry = tk.Entry(window, width=35, font=("Arial", 12), justify="center")
password_entry.pack(pady=10)

# Copy button
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#0984e3", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=5)

# Run the window
window.mainloop()
