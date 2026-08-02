# Calculate Body Mass Index (BMI) from weight and height
# then show Weight Status: Underweight, Healthy Weight, Overweight, or Obesity
# according to the follow link
# https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#InterpretedAdults

from datetime import datetime

# Calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Adult BMI Classification
def adult_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Class 1 Obesity"
    elif bmi < 40:
        return "Class 2 Obesity"
    else:
        return "Class 3 Obesity (Severe Obesity)"


# Calculate exact age
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

# Child BMI Percentile
def calculate_child_percentile(gender, age_years, age_months, bmi):
    # Example placeholder
    # Replace with CDC dataset lookup

    percentile = 50

    return percentile

# Child BMI Classification
def child_bmi_status(percentile, bmi=None):
    if percentile < 5:
        return "Underweight"
    elif percentile < 85:
        return "Healthy Weight"
    elif percentile < 95:
        return "Overweight"
    elif bmi is not None:
        if bmi >= 40:
            return "Class 3 Obesity (Severe Obesity)"
        elif bmi >= 35:
            return "Class 2 Obesity"
        else:
            return "Obesity"
    else:
        return "Obesity"

# Adult Program
def adult_program():

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)

    status = adult_bmi_status(bmi)

    print("\nBMI:", round(bmi, 2))
    print("Weight Status:", status)

# Child Program
def child_program():

    gender = input("Enter gender (Male/Female): ")

    print("\nEnter Date of Birth")

    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    birth_date = datetime(year, month, day)

    age_years, age_months, age_days = calculate_age(birth_date)

    print(
        f"Age: {age_years} years "
        f"{age_months} months "
        f"{age_days} days"
    )

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)

    percentile = calculate_child_percentile(
        gender,
        age_years,
        age_months,
        bmi
    )

    status = child_bmi_status(percentile)

    print("\nBMI:", round(bmi, 2))
    print("BMI Percentile:", percentile)
    print("Weight Status:", status)

# Main Program
def main():

    age = int(input("Enter your age: "))

    if 2 <= age <= 19:
        child_program()
    elif age >= 20:
        adult_program()
    else:
        print("BMI calculator only supports age 2 or older.")


main()