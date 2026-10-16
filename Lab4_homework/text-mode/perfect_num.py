# Calculate and display all perfect numbers from 1-50
# https://en.wikipedia.org/wiki/Perfect_number
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the
# number itself.
# For instance, 6 has divisors 1, 2 and 3 (excluding itself),
# and 1 + 2 + 3 = 6
# so 6 is a perfect number

# Another example, 28 has divisors 1, 2, 4, 7, and 14 (excluding itself),
# and 1 + 2 + 4 + 7 + 14 = 28
# so 28 is a perfect number

# SOLUTION:
# 1) Find all divisors of that num
# 2) Sum all divisiors
# 3) If sum of divisors = num, it's a perfect num

def perfect_number(num):
    divisor = 1
    total = 0
    cal = ""

    while divisor < num:
        if num % divisor == 0:
            total = total + divisor

            if cal == "":
                cal = str(divisor)
            else:
                cal = cal + " + " + str(divisor)

        divisor = divisor + 1

    print("Divisors:", cal)
    print("Calculation:", cal, "=", total)

    if total == num:
        print(num, "is a perfect number.")
    else:
        print(num, "is not a perfect number.")


num = int(input("Enter a number: "))

perfect_number(num)

# while True:
#     num = 1
#     if num > 50:
#         break
#     if is_perfect_number(num):
#         print(num)
#     num += 1

#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#     return divisors_sum == num

# for n in range(1, 51):
#     if is_perfect_number(n):
#         print(n)