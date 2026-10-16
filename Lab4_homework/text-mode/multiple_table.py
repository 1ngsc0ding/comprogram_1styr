# Calculate and display multiplication table from user input
# e.g. if user input 3, your program will display

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
# 3 x 11 = 33
# 3 x 12 = 36

num = int(input("Enter number: "))

def  multiplication_table(num):
    # for i in range(1, 13):
    #     result = num * i
    #     print(f"{num} x {i} = {result}")

    # Using while loop
    i = 1
    while i <= 12:
        result = num * i
        print(f"{num} x {i} = {result}")
        i += 1

multiplication_table(num)