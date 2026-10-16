numbers = [10, 25, 7, 40, 15]

def find_max(arr):
    max_value = arr[0]
    i = 1

    while i < len(arr):
        if arr[i] > max_value:
            max_value = arr[i]
        i = i + 1
    return max_value


def find_min(arr):
    min_value = arr[0]
    i = 1

    while i < len(arr):
        if arr[i] < min_value:
            min_value = arr[i]
        i = i + 1
    return min_value


def find_average(arr):
    total = 0
    i = 0

    while i < len(arr):
        total = total + arr[i]
        i = i + 1
    return total / len(arr)


def find_max_index(arr):
    max_index = 0
    i = 1

    while i < len(arr):
        if arr[i] > arr[max_index]:
            max_index = i
        i = i + 1
    return max_index


def find_min_index(arr):
    min_index = 0
    i = 1

    while i < len(arr):
        if arr[i] < arr[min_index]:
            min_index = i
        i = i + 1
    return min_index


def search_value(arr, target):
    i = 0

    while i < len(arr):
        if arr[i] == target:
            return i
        i = i + 1
    return -1


def count_higher_than_average(arr):
    avg = find_average(arr)

    count = 0
    i = 0

    while i < len(arr):
        if arr[i] > avg:
            count = count + 1
        i = i + 1
    return count

def is_increasing(arr):
    i = 0

    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            return False
        i = i + 1
    return True

def find_variance(arr):
    avg = find_average(arr)

    total = 0
    i = 0

    while i < len(arr):
        difference = arr[i] - avg
        total = total + difference * difference
        i = i + 1
    return total / len(arr)

print("Array =", numbers)
print("Max =", find_max(numbers))
print("Min =", find_min(numbers))
print("Average =", find_average(numbers))
print("Max index =", find_max_index(numbers))
print("Min index =", find_min_index(numbers))

target = int(input("Enter value to search: "))
result = search_value(numbers, target)

if result == -1:
    print("Not found")
else:
    print("Found at index =", result)

print("Higher than average =", count_higher_than_average(numbers))

if is_increasing(numbers):
    print("Array is increasing")
else:
    print("Array is not increasing")
print("Variance =", find_variance(numbers))