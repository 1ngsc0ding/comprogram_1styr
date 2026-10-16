class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        print("License plate:", self.license_plate)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Daily rate:", self.daily_rate, "baht")

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print("Seats:", self.seats)

    def calculate_rental_cost(self, days):
        if days == 5:
            return self.daily_rate * 5
        return super().calculate_rental_cost(days)


class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year,daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        super().show_info()
        print("Payload:", self.payload, "kg")

car1 = Car("กข1234", "Toyota", "Yaris", 2024, 1000, 5)

truck1 = Truck("ฮฮ5678", "Isuzu", "NPR", 2023, 2000, 3000)

print("Car Information")
car1.show_info()
print("Rental cost for 5 days:", car1.calculate_rental_cost(5), "baht")

print("\nTruck Information")
truck1.show_info()
print("Rental cost for 5 days:", truck1.calculate_rental_cost(5), "baht")