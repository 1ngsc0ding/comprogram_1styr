num_arr = [10, 30, 20, 50, 40]

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return median

answer = find_median(num_arr)

print(f"{answer:.2f} is the median of {num_arr}")