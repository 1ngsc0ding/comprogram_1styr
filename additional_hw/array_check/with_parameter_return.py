numbers = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]

def check_number(numbers):
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] > 500:
            result.append(numbers[i])
        i += 1
    return result

print(f"{check_number(numbers)} are greater than 500") # [800, 600, 900, 550, 650, 601] are greater than 500

# Print line-by-line
result = check_number(numbers)
while result:
    print(f"{result[0]} is greater than 500")
    result.pop(0)