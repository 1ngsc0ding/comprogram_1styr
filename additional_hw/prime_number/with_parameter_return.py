def get_prime(max_number):
    primes = []
    n = 2

    while n <= max_number:
        is_prime = True
        divisor = 2

        while divisor < n:
            if n % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            primes.append(n)
        n += 1
    return primes

result = get_prime(100)

print(result)