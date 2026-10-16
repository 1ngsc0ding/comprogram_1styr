# Write Python program (with appropriate inputs, outputs and functions)
# - write functions to
# a. find max/min/average value of a 2D array

# b. check whether a value is in a 2D array (return boolean)
# is_found( my_array, 55 )

# c. matrix add, subtract, multiplication

# Input 2D arrays
# Insert each number in the 2D array by user input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

numbers = []

for row_num in range(rows):
    row = []
    for col_num in range(cols):
        num = int(input(f"Enter element at position ({row_num}, {col_num}): "))
        row.append(num)
    numbers.append(row)


def find_max(a):
    maximum = a[0][0]

    for row_num in range(len(a)):
        for col_num in range(len(a[row_num])):
            if a[row_num][col_num] > maximum:
                maximum = a[row_num][col_num]
    return maximum
print("Max =", find_max(numbers))


def find_min(a):
    minimum = a[0][0]

    for row_num in range(len(a)):
        for col_num in range(len(a[row_num])):
            if a[row_num][col_num] < minimum:
                minimum = a[row_num][col_num]
    return minimum
print("Min =", find_min(numbers))

def find_average(a):
    total = 0
    count = 0

    for row_num in range(len(a)):
        for col_num in range(len(a[row_num])):
            total += a[row_num][col_num]
            count += 1
    return total / count
print("Average =", find_average(numbers))


def is_found(a, value):
    for row_num in range(len(a)):
        for col_num in range(len(a[row_num])):
            if a[row_num][col_num] == value:
                return True
    return False

value = int(input("Enter value to find: "))
print("Found =", is_found(numbers, value))

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

add = []
for row_num in range(len(a)):
    row = []
    for col_num in range(len(a[row_num])):
        row.append(a[row_num][col_num] + b[row_num][col_num])
    add.append(row)
print("Add =", add)

sub = []
for row_num in range(len(a)):
    row = []
    for col_num in range(len(a[row_num])):
        row.append(a[row_num][col_num] - b[row_num][col_num])
    sub.append(row)
print("Subtract =", sub)

mul = []

for row_num in range(len(a)):
    row = []
    for col_num in range(len(b[0])):
        total = 0
        for num in range(len(b)):
            total += a[row_num][num] * b[num][col_num]
        row.append(total)
    mul.append(row)
print("Multiply =", mul)
