import random


total_sum = 0
x = 0


def Choice(n):
    # Select either Random Mode or Input Mode.
    if n == 1:
        Random_Mode()

    if n == 2:
        Input_Mode()
    else:
        # Display an error when the selected choice is unavailable.
        print("Error: there is no choice", n)


def Random_Mode():
    # Generate random integers until -1 appears.
    global total_sum
    global x

    while x != -1:
        x = random.randint(-1, 10)
        print(x)
        total_sum += x

    print("Sum of random mode is:", total_sum)


def Input_Mode():
    # Receive integers from the user until -1 is entered.
    global total_sum
    global x

    while x != -1:
        x = int(input("Input any integer, or input -1 to end: "))
        total_sum += x

    print("Sum of this session is:", total_sum)


# Receive the operating mode directly from the user.
Choice(float(input("Input 1 for Random Mode, or input 2 for Input Mode: ")))
