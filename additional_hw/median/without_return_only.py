num_arr = [10, 30, 20, 50, 40]

def find_median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    print(f"{median:.2f} is the median of {numbers}")

find_median(num_arr)