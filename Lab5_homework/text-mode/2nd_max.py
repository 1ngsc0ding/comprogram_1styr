numbers = [10, 25, 7, 40, 15, 35]

def find_second_max(arr):

    max_value = arr[0]
    second_max = arr[1]

    if second_max > max_value:
        temp = max_value
        max_value = second_max
        second_max = temp

    i = 2

    while i < len(arr):
        if arr[i] > max_value:
            second_max = max_value
            max_value = arr[i]
        elif arr[i] > second_max and arr[i] < max_value:
            second_max = arr[i]
        i = i + 1
    return second_max

result = find_second_max(numbers)

print("Second maximum =", result)