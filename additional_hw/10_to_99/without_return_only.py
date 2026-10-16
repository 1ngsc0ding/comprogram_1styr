import random

def random_numbers(amount):
    numbers = []
    i = 0
    while i < amount:
        num = random.randint(10, 99)
        numbers.append(num)
        i += 1
    print(numbers)

random_numbers(20)