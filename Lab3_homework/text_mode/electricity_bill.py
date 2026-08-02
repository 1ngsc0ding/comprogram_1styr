def calculate_bill(unit):
    if unit <= 150:
        rate = 3.25
    elif unit <= 400:
        rate = 4.22
    else:
        rate = 4.42

    bill = unit * rate

    if bill >= 1000:
        if unit > 500:
            discount = bill * 0.10
        else:
            discount = bill * 0.05
    else:
        discount = 0

    total = bill - discount
    return rate, discount, total

try:
    unit = float(input("Enter electricity usage (kWh): "))

    if unit < 0:
        print("Error: Electricity usage cannot be negative.")
    else:
        rate, discount, total = calculate_bill(unit)

        print("\n------ Electricity Bill ------")
        print(f"Usage      : {unit:.0f} kWh")
        print(f"Rate       : {rate:.2f} THB/kWh")
        print(f"Discount   : {discount:.2f} THB")
        print(f"Total Bill : {total:.2f} THB")

        if total >= 1500 and unit > 300:
            print("Status: High electricity usage")
        elif total >= 500 or unit > 150:
            print("Status: Medium electricity usage")
        elif not (unit > 150):
            print("Status: Low electricity usage")

except ValueError:
    print("Error: Please enter a valid number.")