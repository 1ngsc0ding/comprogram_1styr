import tkinter as tk
from tkinter import messagebox

class Vehicle:
    def __init__(self, license_plate, brand, model,
                 year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        return (
            f"License plate: {self.license_plate}\n"
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}\n"
            f"Daily rate: {self.daily_rate:.2f} baht"
        )

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

class Car(Vehicle):
    def __init__(self, license_plate, brand, model,
                 year, daily_rate, seats):
        super().__init__(license_plate, brand, model,
                         year, daily_rate)
        self.seats = seats

    def show_info(self):
        return super().show_info() + f"\nSeats: {self.seats}"

    def calculate_rental_cost(self, days):
        if days == 5:
            return self.daily_rate * 5
        return super().calculate_rental_cost(days)

class Truck(Vehicle):
    def __init__(self, license_plate, brand, model,
                 year, daily_rate, payload):
        super().__init__(license_plate, brand, model,
                         year, daily_rate)
        self.payload = payload

    def show_info(self):
        return super().show_info() + f"\nPayload: {self.payload} kg"

def calculate():
    try:
        plate = entries["License plate"].get()
        brand = entries["Brand"].get()
        model = entries["Model"].get()
        year = int(entries["Year"].get())
        rate = float(entries["Daily rate"].get())
        days = int(entries["Rental days"].get())

        if not plate or not brand or not model:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if rate < 0 or days <= 0:
            messagebox.showerror("Error", "Invalid rate or rental days.")
            return

        if vehicle_type.get() == "Car":
            seats = int(entries["Seats / Payload"].get())
            vehicle = Car(plate, brand, model, year, rate, seats)
        else:
            payload = float(entries["Seats / Payload"].get())
            vehicle = Truck(plate, brand, model, year, rate, payload)

        result = vehicle.show_info()
        result += f"\nRental days: {days}"
        result += (
            f"\nTotal cost: "
            f"{vehicle.calculate_rental_cost(days):,.2f} baht"
        )

        output.delete("1.0", tk.END)
        output.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Vehicle Rental")
root.geometry("450x600")

tk.Label(root, text="Vehicle Rental",
         font=("Arial", 18, "bold")).pack(pady=10)

vehicle_type = tk.StringVar(value="Car")

tk.Label(root, text="Vehicle Type").pack()
tk.OptionMenu(root, vehicle_type, "Car", "Truck").pack()

entries = {}

fields = [
    "License plate", "Brand", "Model", "Year",
    "Daily rate", "Seats / Payload", "Rental days"
]

for field in fields:
    tk.Label(root, text=field).pack()
    entry = tk.Entry(root, width=30)
    entry.pack(pady=3)
    entries[field] = entry

tk.Label(
    root,
    text="Seats for Car / Payload (kg) for Truck"
).pack(pady=3)

tk.Button(root, text="Calculate Rental Cost",
          command=calculate).pack(pady=10)

output = tk.Text(root, height=12, width=45)
output.pack(pady=5)

root.mainloop()