# Week 01: text output, variables, and simple calculations
def main():
    print("Hello, World")
    print("Hello, KMUTNB")
    print("KMUT" + "NB")
    print("1" + "2")
    print(1 + 2)

    x = 200
    y = 100
    height = 200
    width = 100
    print("left line endpoints:", (x, y), (x, y + height))
    print("right line endpoints:", (x + width, y), (x + width, y + height))

if __name__ == "__main__":
    main()
