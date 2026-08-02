# Calculate Body Mass Index (BMI) from weight and height

#Acquire user input for weight and height
weight = float(input("Insert weight (kg): "))
height = float(input("Insert height (cm): "))

height = height / 100  # Convert height from cm to m

bmi = weight / (height ** 2) # Calculate BMI

print("Your BMI is =", bmi) # Display BMI