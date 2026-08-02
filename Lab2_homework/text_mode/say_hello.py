# Write Python program (with appropriate variables and outputs) containing function

# - say_hello( choice )
# function name: say_hello
# parameter name: choice
# when choice equal 1, it will print out "Hello, KMUTNB"
# when choice equal 2, it will print out "Sawasdee, KMUTNB"
# when choice equal 3, it will print out "<hello in another language>, KMUTNB"
# when choice equal 4, it will print out "Error: there is no choice 4, please try
# again"

# Define the say_hello function that takes a choice parameter
def say_hello(choice): 
    if choice == 1:
        print("Hello, KMUTNB")
    elif choice == 2:
        print("Sawasdee, KMUTNB")
    elif choice == 3:
        print("Bonjour, KMUTNB")
    else:
        print("Error: there is no choice 4, please try again")

choice = int(input("Enter some choice: ")) # Acquire user input for choice
say_hello(choice) # Call the say_hello function with the user's choice