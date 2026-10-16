import tkinter as tk
from tkinter import messagebox

class mySet:
    def __init__(self):
        self.items = []

    def show(self):
        return str(self.items)

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

s = mySet()

def add_item():
    try:
        item = int(entry.get())
        s.add(item)
        update_list()
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer.")

def remove_item():
    try:
        item = int(entry.get())
        if item not in s.items:
            messagebox.showinfo("Information", "Item not found.")
        else:
            s.remove(item)
            update_list()
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer.")

def update_list():
    output.delete("1.0", tk.END)
    output.insert(tk.END, s.show())

root = tk.Tk()
root.title("My Set")
root.geometry("350x350")

tk.Label(root, text="My Set",
         font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Enter an integer").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Add Item",
          command=add_item).pack(pady=5)

tk.Button(root, text="Remove Item",
          command=remove_item).pack(pady=5)

tk.Label(root, text="Items in Set").pack(pady=5)
output = tk.Text(root, height=5, width=30)
output.pack()

update_list()
root.mainloop()