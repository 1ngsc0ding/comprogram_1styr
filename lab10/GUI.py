import tkinter as tk

def count_character():
    text = entry_text.get()
    char = entry_char.get()

    if char == "":
        result_label.config(text="Please enter a character")
    else:
        count = text.count(char)
        result_label.config(text=f"Character count: {count}")

def count_vowels():
    text = entry_text.get()
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1
    result_label.config(text=f"Vowel count: {count}")

def check_palindrome():
    text = entry_text.get()
    text = text.lower().replace(" ", "")

    if text == text[::-1]:
        result_label.config(text="It is a Palindrome")
    else:
        result_label.config(text="It is not a Palindrome")

window = tk.Tk()
window.title("GUI Text Analyzer")
window.geometry("400x300")

label_text = tk.Label(window, text="Enter text:")
label_text.pack(pady=5)

entry_text = tk.Entry(window, width=30)
entry_text.pack(pady=5)

label_char = tk.Label(window, text="Enter character to count:")
label_char.pack(pady=5)

entry_char = tk.Entry(window, width=10)
entry_char.pack(pady=5)

button_character = tk.Button(window, text="Count Character", command=count_character)
button_character.pack(pady=5)

button_vowels = tk.Button(window, text="Count Vowels", command=count_vowels)
button_vowels.pack(pady=5)

button_palindrome = tk.Button(window, text="Check Palindrome", command=check_palindrome)
button_palindrome.pack(pady=5)

result_label = tk.Label(window, text="Result:")
result_label.pack(pady=15)

window.mainloop()