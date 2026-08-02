# จงเขียนโปรแกรมและรับค่าสำหรับการหาค่า BMI

weight = float(input("Insert your weight(kg): ")) # Acquire user input for weight in kilograms
height_cm = float(input("Insert your height(cm): ")) # Acquire user input for height in centimeters
height_m = height_cm / 100 # Convert height from centimeters to meters

bmi = weight / (height_m ** 2) # Calculate BMI using weight (kg) / (height (m))^2

print(f"Your BMI is {bmi:.2f}") # Display the BMI rounded to two decimal places