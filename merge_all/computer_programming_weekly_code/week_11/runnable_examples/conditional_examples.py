# Standalone Python equivalent of conditional examples
def classify_x(x):
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")

def main():
    for value in (10, -2, 0):
        classify_x(value)
    a, b, i, j = 4, 7, 3, 9
    x = (a + b)
    y = ((i + j) * (i - a) / 5)
    print("x =", x)
    print("y =", y)

if __name__ == "__main__":
    main()
