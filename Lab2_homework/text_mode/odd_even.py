# If the number is divisible by 2, print "Even"; otherwise, print "Odd"

number = int(input("Enter number: ")) # Acquire user input for the number

# Check if the number is even by using the modulus operator
if number % 2 == 0: 
    print("Even")
else:
    print("Odd")