# Calculate and display the sum from 1 to n

def Sum_of_1_to_n(n):    
    total_sum = 1
    print("Sum of 1 to", n, "is", end=" ")

    # Sum positive integers from n down to 1.
    while n > 1:
        total_sum += n
        n = n - 1

    # Sum negative integers from n up to 1.
    while n < 1:
        total_sum += n
        n = n + 1

    print(total_sum)

    # Acquire the value from the user.
    Sum_of_1_to_n(int(input("You want to know sum of 1 to ")))


# Receive the first value from the user.
Sum_of_1_to_n(int(input("You want to know sum of 1 to ")))
