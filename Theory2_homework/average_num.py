# จงเขียนโปรแกรมและรับค่าสำหรับการหาค่าเฉลี่ยของเลข 3 จำนวน

n1 = float(input("Enter the first number: ")) # Acquire user input for the first number
n2 = float(input("Enter the second number: ")) # Acquire user input for the second number
n3 = float(input("Enter the third number: ")) # Acquire user input for the third number

average = (n1 + n2 + n3) / 3 # Calculate the average of the three numbers

print(f"Average = {average:.2f}") # Display the average rounded to two decimal places