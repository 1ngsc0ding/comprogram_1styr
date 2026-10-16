import random

def random_numbers():
    numbers = []
    i = 0
    while i < 20:
        num = random.randint(10, 99)
        numbers.append(num)
        i += 1
    print(numbers)

random_numbers()