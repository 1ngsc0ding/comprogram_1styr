import random

numbers = []
count = 0
index = 0

while count < 10:
    num = random.randint(100, 1000)
    numbers.append(num)
    count += 1

while index < len(numbers):
    if numbers[index] > 800:
        print(f"{numbers[index]} is greater than 800")
    index += 1