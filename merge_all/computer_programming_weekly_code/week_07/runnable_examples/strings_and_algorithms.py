# Week 07: strings, concatenation, factorial, and basic algorithms
def factorial_loop(number):
    if number < 0:
        raise ValueError("factorial is defined here only for non-negative integers")
    result = 1
    count = 2
    while count <= number:
        result *= count
        count += 1
    return result

def factorial_recursive(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

def is_sorted(values):
    index = 0
    while index < len(values) - 1:
        if values[index] > values[index + 1]:
            return False
        index += 1
    return True

if __name__ == "__main__":
    text = "Hello"
    print("Characters:")
    index = 0
    while index < len(text):
        print(index, text[index])
        index += 1
    print("Concatenation:", text + " Joe")
    print("Factorial loop:", factorial_loop(5))
    print("Factorial recursion:", factorial_recursive(5))
    print("Sorted?", is_sorted([1, 2, 3]))
