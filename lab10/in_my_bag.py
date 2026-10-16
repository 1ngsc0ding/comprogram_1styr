import tkinter as tk
from tkinter import messagebox

class myBag:
    def __init__(self):
        self.items = []

    def show(self):
        return str(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

bag = myBag()

def add_item():
    try:
        item = int(entry.get())
        bag.add(item)
        update_list()
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer.")

def remove_item():
    try:
        item = int(entry.get())
        if bag.remove(item):
            update_list()
        else:
            messagebox.showinfo("Information", "Item not found.")
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer.")

def update_list():
    output.delete("1.0", tk.END)
    output.insert(tk.END, bag.show())

root = tk.Tk()
root.title("My Bag")
root.geometry("350x350")

tk.Label(root, text="My Bag",
         font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Enter an integer").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Add Item",
          command=add_item).pack(pady=5)

tk.Button(root, text="Remove Item",
          command=remove_item).pack(pady=5)

tk.Label(root, text="Items in Bag").pack(pady=5)
output = tk.Text(root, height=5, width=30)
output.pack()

update_list()
root.mainloop()