import tkinter as tk

count = 0

def increase():
    global count
    count = count + 1
    number_label.config(text=count)

def decrease():
    global count
    count = count - 1
    number_label.config(text=count)

def reset():
    global count
    count = 0
    number_label.config(text=count)

window = tk.Tk()
window.title("Counter App")
window.geometry("300x230")

number_label = tk.Label(window, text=count, font=("Arial", 24))
number_label.pack(pady=20)

increase_button = tk.Button(window, text="Increase", command=increase)
increase_button.pack(pady=5)

decrease_button = tk.Button(window, text="Decrease", command=decrease)
decrease_button.pack(pady=5)

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.pack(pady=5)

window.mainloop()