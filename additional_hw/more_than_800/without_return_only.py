import random

def check_random_number(amount):
    numbers = []
    count = 0
    index = 0

    while count < amount:
        num = random.randint(100, 1000)
        numbers.append(num)
        count += 1

    print(numbers)

    while index < len(numbers):
        if numbers[index] > 800:
            print(f"{numbers[index]} is greater than 800")
        index += 1

check_random_number(10)