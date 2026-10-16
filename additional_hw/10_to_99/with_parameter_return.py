import random

def create_numbers(amount):
    numbers = []
    i = 0
    while i < amount:
        num = random.randint(10, 99)
        numbers.append(num)
        i += 1
    return numbers

data = create_numbers(20)
print(data)