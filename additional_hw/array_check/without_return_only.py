numbers = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]

def check_number(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] > 500:
            print(f"{numbers[i]} is greater than 500")
        i += 1

check_number(numbers)