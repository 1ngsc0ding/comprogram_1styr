import tkinter as tk

def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9 / 5) + 32
        result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")
    except ValueError:
        result_label.config(text="Please enter a number")

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("270x150")

label_celsius = tk.Label(window, text="Celsius:")
label_celsius.pack(pady=5)

entry_celsius = tk.Entry(window)
entry_celsius.pack(pady=5)

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="Fahrenheit:")
result_label.pack(pady=5)

window.mainloop()
