import random


def random_x():
    # Generate a random integer and identify whether it is negative.
    x = random.randint(-5, 5)

    print(x)

    if x < 0:
        print("x is negative")
    else:
        print("x is not negative")

    # Allow the user to run the program again.
    n = int(input("Input 1 to try again: "))

    if n == 1:
        random_x()
    else:
        print("End")


random_x()
