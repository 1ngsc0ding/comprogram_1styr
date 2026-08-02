def print_line(n):
    # Print n asterisks on one line.
    while n > 0:
        print("*", end="")
        n = n - 1

    print()
    print("Test done")


# Receive the number of asterisks from the user.
print_line(int(input("Enter the number of *: ")))
