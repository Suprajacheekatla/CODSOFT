import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Update listbox
def update_listbox():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, f"{name} - {contacts[name]['Phone']}")

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts()
    update_listbox()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully!")

# Search Contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if query:
        for name, info in contacts.items():
            if query.lower() in name.lower() or query in info['Phone']:
                name_entry.delete(0, tk.END)
                name_entry.insert(0, name)
                phone_entry.delete(0, tk.END)
                phone_entry.insert(0, info["Phone"])
                email_entry.delete(0, tk.END)
                email_entry.insert(0, info["Email"])
                address_entry.delete(0, tk.END)
                address_entry.insert(0, info["Address"])
                return
        messagebox.showinfo("Not Found", "No matching contact found.")

# Delete Contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        confirm = messagebox.askyesno("Delete", f"Are you sure to delete {name}?")
        if confirm:
            del contacts[name]
            save_contacts()
            update_listbox()
            clear_fields()
            messagebox.showinfo("Deleted", f"{name} has been deleted.")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Update Contact
def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            "Phone": phone_entry.get(),
            "Email": email_entry.get(),
            "Address": address_entry.get()
        }
        save_contacts()
        update_listbox()
        messagebox.showinfo("Updated", f"{name}'s details updated.")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("600x450")
root.config(bg="#f0f4f7")

# Data
contacts = load_contacts()

# Labels and Inputs
tk.Label(root, text="Name", font=("Arial", 12), bg="#f0f4f7").place(x=20, y=20)
name_entry = tk.Entry(root, width=30)
name_entry.place(x=150, y=20)

tk.Label(root, text="Phone Number", font=("Arial", 12), bg="#f0f4f7").place(x=20, y=60)
phone_entry = tk.Entry(root, width=30)
phone_entry.place(x=150, y=60)

tk.Label(root, text="Email", font=("Arial", 12), bg="#f0f4f7").place(x=20, y=100)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=150, y=100)

tk.Label(root, text="Address", font=("Arial", 12), bg="#f0f4f7").place(x=20, y=140)
address_entry = tk.Entry(root, width=30)
address_entry.place(x=150, y=140)

# Buttons
tk.Button(root, text="Add Contact", width=15, bg="#4caf50", fg="white", command=add_contact).place(x=420, y=20)
tk.Button(root, text="Update Contact", width=15, bg="#2196f3", fg="white", command=update_contact).place(x=420, y=60)
tk.Button(root, text="Delete Contact", width=15, bg="#f44336", fg="white", command=delete_contact).place(x=420, y=100)
tk.Button(root, text="Search Contact", width=15, bg="#ff9800", fg="white", command=search_contact).place(x=420, y=140)

# Contact List
tk.Label(root, text="Saved Contacts", font=("Arial", 12, "bold"), bg="#f0f4f7").place(x=20, y=190)
contact_list = tk.Listbox(root, width=70, height=12)
contact_list.place(x=20, y=220)

update_listbox()
root.mainloop()
