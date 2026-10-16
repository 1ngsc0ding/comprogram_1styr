# Maximum value and non-decreasing sorted check
def find_max(values):
    if not values:
        raise ValueError("values must not be empty")
    maximum = values[0]
    index = 1
    while index < len(values):
        if values[index] > maximum:
            maximum = values[index]
        index += 1
    return maximum

def is_sorted(values):
    index = 0
    while index < len(values) - 1:
        if values[index] > values[index + 1]:
            return False
        index += 1
    return True

if __name__ == "__main__":
    data = [5, 9, 2]
    print("Maximum:", find_max(data))
    print("Sorted:", is_sorted(data))
    print("Sorted example:", is_sorted([1, 2, 2, 4]))
