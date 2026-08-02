from datetime import datetime
from bmi import (
    calculate_bmi,
    adult_bmi_status,
    child_bmi_status,
    obesity_class_child
)
from percentile import calculate_percentile



def calculate_age(birth_date):
    today = datetime.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1

    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days



def child_program():
    print("\n--- Child and Teen BMI Calculator ---")
    gender = input("Enter gender (male/female): ").strip().lower()

    print("\nEnter date of birth")
    date_input = input("Enter date (example: 25 February 2008): ").strip()

    try:
        birth_date = datetime.strptime(date_input, "%d %B %Y")
    except ValueError:
        try:
            birth_date = datetime.strptime(date_input, "%d %b %Y")
        except ValueError:
            try:
                birth_date = datetime.strptime(date_input, "%d/%m/%Y")
            except ValueError:
                try:
                    birth_date = datetime.strptime(date_input, "%d-%m-%Y")
                except ValueError:
                    try:
                        day, month, year = [int(part) for part in date_input.split()]
                        birth_date = datetime(year, month, day)
                    except ValueError as exc:
                        raise ValueError("Please enter a valid date like 25 February 2008") from exc

    age_year, age_month, age_day = calculate_age(birth_date)

    print(
        f"\nAge: {age_year} years "
        f"{age_month} months "
        f"{age_day} days"
    )


    weight = float(input("\nEnter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = calculate_bmi(weight, height)
    total_month = (age_year * 12 + age_month)
    percentile = calculate_percentile(gender, total_month, bmi)
    status = child_bmi_status(percentile, bmi)

    print("\n----------- Result -----------")
    print("BMI:", round(bmi, 2))
    print("BMI Percentile:", percentile)
    print("Weight Status:", status)

    if status == "Obesity":
        obesity = obesity_class_child(bmi, percentile)
        print("Obesity Classification:", obesity)



def adult_program():
    print("\n--- Adult BMI Calculator ---")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = calculate_bmi(weight, height)
    status = adult_bmi_status(bmi)

    print("\n----------- Result -----------")
    print("BMI:", round(bmi, 2))
    print("Weight Status:", status)

def main():
    print("\n       BMI Calculator")
    print("==============================")
    age = int(input("Enter age: "))

    if 2 <= age <= 19:
        child_program()
    elif age >= 20:
        adult_program()
    else:
        print("This program only supports age 2 or older.")

if __name__ == "__main__":
    main()