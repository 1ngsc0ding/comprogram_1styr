import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def getBMI(self):
        if self.height <= 0:
            return 0
        return self.weight / (self.height ** 2)

class Student(Person):
    def __init__(self, name, address, weight, height,
                 student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        return (
            f"Student Information\n"
            f"Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Weight: {self.weight} kg\n"
            f"Height: {self.height} m\n"
            f"Student ID: {self.student_id}\n"
            f"Course: {self.course}\n"
            f"GPA: {self.gpa}\n"
            f"BMI: {self.getBMI():.2f}"
        )

class Employee(Person):
    def __init__(self, name, address, weight, height,
                 employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        return (
            f"Employee Information\n"
            f"Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Weight: {self.weight} kg\n"
            f"Height: {self.height} m\n"
            f"Employee ID: {self.employee_id}\n"
            f"Department: {self.department}\n"
            f"Salary: {self.salary:.2f} baht\n"
            f"BMI: {self.getBMI():.2f}"
        )

def display_info():
    try:
        name = entries["Name"].get()
        address = entries["Address"].get()
        weight = float(entries["Weight (kg)"].get())
        height = float(entries["Height (m)"].get())

        if not name or not address:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive.")
            return

        if person_type.get() == "Student":
            person = Student(
                name, address, weight, height,
                entries["ID"].get(),
                entries["Course / Department"].get(),
                float(entries["GPA / Salary"].get())
            )
        else:
            person = Employee(
                name, address, weight, height,
                entries["ID"].get(),
                entries["Course / Department"].get(),
                float(entries["GPA / Salary"].get())
            )

        output.delete("1.0", tk.END)
        output.insert(tk.END, person.show())

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Personal Information")
root.geometry("500x650")

tk.Label(root, text="Personal Information",
         font=("Arial", 18, "bold")).pack(pady=10)

person_type = tk.StringVar(value="Student")

tk.Label(root, text="Person Type").pack()
tk.OptionMenu(root, person_type, "Student", "Employee").pack()

entries = {}

fields = [
    "Name", "Address", "Weight (kg)", "Height (m)",
    "ID", "Course / Department", "GPA / Salary"
]

for field in fields:
    tk.Label(root, text=field).pack()
    entry = tk.Entry(root, width=35)
    entry.pack(pady=3)
    entries[field] = entry

tk.Button(root, text="Show Information",
          command=display_info).pack(pady=10)

output = tk.Text(root, height=12, width=50)
output.pack(pady=5)

root.mainloop()