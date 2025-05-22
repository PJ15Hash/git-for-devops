import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    if not name or not email or not age:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    if not age.isdigit():
        messagebox.showwarning("Input Error", "Age must be a number")
        return

    message = f"Name: {name}\nEmail: {email}\nAge: {age}"
    messagebox.showinfo("Form Submitted", message)


# Create main window
root = tk.Tk()
root.title("Basic Form")


# Labels and entries
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0, sticky="e")
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)


# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()

password - 123