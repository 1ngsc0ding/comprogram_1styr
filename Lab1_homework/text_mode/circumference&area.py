# Calculate circumference and area of a circle from its diameter (not radius)

import math # Professor did not declare the value of pi, so I imported the math module to use math.pi

d = float(input("Enter diameter: ")) # Acquire user input for diameter

circumference = 2 * math.pi * (d / 2) # Calculate circumference
area = math.pi * (d / 2) ** 2 # Calculate area

print("Circumference is", circumference) # Display circumference
print("Area is", area) # Display area