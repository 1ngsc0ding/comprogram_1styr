n = 2

while n <= 100:
    is_prime = True
    divisor = 2

    while divisor < n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(n)
    n += 1