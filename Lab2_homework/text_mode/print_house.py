# - print_house( h )
# function name: print_house
# parameter name: h
# when h equal 1, it will display
#   ^
#  ^ ^
# ^   ^
# |||||
# |   |
# |   |
# |||||
# when h equal 2, it will display
#   ^
#  ^ ^
# ^   ^
# |||||
# |   |
# |   |
# |||||
# |   |
# |   |
# |||||
# when h equal 3, it will display
#   ^
#  ^ ^
# ^   ^
# |||||
# |   |
# |   |
# |||||
# |   |
# |   |
# |||||
# |   |
# |   |
# |||||
# Your program should create and call the following user-defined functions
# print_roof(), print_ceiling(), print_wall(), print_floor()
# with a appropriate parameter/argument

# Define the print_roof function that displays the roof of the house
def print_roof(): 
    print("  ^  ")
    print(" ^ ^ ")
    print("^   ^")

# Define the print_ceiling function that displays the ceiling of the house
def print_ceiling(): 
    print("|||||")

# Define the print_wall function that displays the walls of the house
def print_wall(): 
    print("|   |")
    print("|   |")

# Define the print_floor function that displays the floor of the house
def print_floor(): 
    print("|||||")

# Define the print_house_recursive function that takes a height parameter
def print_house_recursive(height): 
    print_roof()
    print_ceiling()
    print_body(height)

# Define the print_body function that takes a height parameter and prints the walls and floor recursively
def print_body(height): 
    if height == 0:
        return

    print_wall()
    print_floor()
    print_body(height - 1)

# We can use loop as well
# Define the print_house function that takes a height parameter and prints the house using a loop
# def print_house(height):
#     print_roof()
#     print_ceiling()

#     for _ in range(height):
#         print_wall()
#         print_floor()

height = int(input("Enter height of the house: ")) # Acquire user input for the height of the house
# print_house(height) # Use with loop
print_house_recursive(height)