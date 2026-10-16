def find_median():
    n = int(input("Enter amount of numbers: "))
    numbers = []
    i = 0

    while i < n:
        num = float(input("Enter number: "))
        numbers.append(num)
        i += 1

    numbers.sort()
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    print(f"{median:.2f} is the median of {numbers}")

find_median()