import tkinter as tk
from tkinter import ttk
import database_manager

def load_data():
    emails = database_manager.fetch_all_emails()
    for row in emails:
        tree.insert("", "end", values=row)

# GUI Setup
root = tk.Tk()
root.title("Saved Predictions")
root.geometry("800x400")

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Table
tree = ttk.Treeview(root, columns=("ID", "Email", "Prediction"), show="headings", yscrollcommand=scrollbar.set)
tree.heading("ID", text="ID")
tree.heading("Email", text="Email")
tree.heading("Prediction", text="Prediction")

tree.column("ID", width=50)
tree.column("Email", width=500)
tree.column("Prediction", width=100)

tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

load_data()
root.mainloop()
