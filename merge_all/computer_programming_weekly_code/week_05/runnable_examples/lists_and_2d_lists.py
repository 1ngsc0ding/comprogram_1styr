# Week 05: list processing and nested loops
def print_all(values):
    index = 0
    while index < len(values):
        print(values[index])
        index += 1

def print_2d(matrix):
    row = 0
    while row < len(matrix):
        column = 0
        while column < len(matrix[row]):
            print(matrix[row][column], end=" ")
            column += 1
        print()
        row += 1

def main():
    values = [5, 9, 2]
    print("List elements:")
    print_all(values)

    matrix = [[5, 7, 9], [2, 4, 6], [8, 3, 1]]
    matrix[1][2] = 7
    matrix[2][2] = 5
    print("2D list:")
    print_2d(matrix)

if __name__ == "__main__":
    main()
