# Week 03: Tkinter GUI multiplier
# Run with Python on a desktop with Tk support.
import tkinter as tk
from tkinter import messagebox

def multiply():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter two numbers.")
        return
    result_label.config(text=f"Result: {number1 * number2:g}")

window = tk.Tk()
window.title("Multiply two numbers")
window.geometry("320x220")

form = tk.Frame(window, padx=12, pady=12)
form.pack(fill="both", expand=True)
tk.Label(form, text="First number").grid(row=0, column=0, sticky="w", pady=5)
entry1 = tk.Entry(form, width=18)
entry1.grid(row=0, column=1, pady=5)
tk.Label(form, text="Second number").grid(row=1, column=0, sticky="w", pady=5)
entry2 = tk.Entry(form, width=18)
entry2.grid(row=1, column=1, pady=5)
tk.Button(form, text="Multiply", command=multiply).grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(form, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2)
window.mainloop()
