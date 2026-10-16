# Week 09: if/else, while loops, and accumulation
def describe_number(number):
    if number > 0:
        return "x is positive"
    elif number < 0:
        return "x is negative"
    return "x is zero"

def sum_1_to_n(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

def countdown(start):
    while start > 0:
        print(start)
        start -= 1

if __name__ == "__main__":
    for value in (5, -3, 0):
        print(value, describe_number(value))
    countdown(5)
    print("Sum =", sum_1_to_n(5))
