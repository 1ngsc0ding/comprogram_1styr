import random

def check_random_number(amount):
    numbers = []
    warning = []
    count = 0
    index = 0

    while count < amount:
        num = random.randint(100, 1000)
        numbers.append(num)
        count += 1

    while index < len(numbers):
        if numbers[index] > 800:
            warning.append(numbers[index])
        index += 1
    return numbers, warning

numbers, warning = check_random_number(10)

print(numbers)

while warning:
    print(f"{warning[0]} is greater than 800")
    warning.pop(0)