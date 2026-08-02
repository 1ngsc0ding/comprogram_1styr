# Password Analyzer
def check_ascii(password, start, end):
    # Check if the character's ASCII value is within the specified range
    for character in password: 
        # If the character's ASCII value is within the range, return True
        if start <= ord(character) <= end: 
            return True
    # If no character's ASCII value is within the range, return False
    return False 

# Check if the password contains at least one special character
def check_special(password):
    # Check if the character's ASCII value is within the range of special characters
    for character in password:
        # Get the ASCII value of the character
        code = ord(character)
        # If the ASCII value is within the range of special characters, return True
        if (33 <= code <= 47 or
            58 <= code <= 64 or
            91 <= code <= 96 or
            123 <= code <= 126):
            return True
    # If no character's ASCII value is within the range of special characters,
    return False

# Check the password against the specified criteria
def password_checker(password):
    # Check if the password meets the criteria for length, uppercase letter, lowercase letter, number, and special character
    if len(password) < 8:
        print("Missing: at least 8 characters")
    elif not check_ascii(password, 65, 90):
        print("Missing: uppercase letter")
    elif not check_ascii(password, 97, 122):
        print("Missing: lowercase letter")
    elif not check_ascii(password, 48, 57):
        print("Missing: number")
    elif not check_special(password):
        print("Missing: special character")
    else:
        print("Password Accepted")

password = input("Enter password: ") # Acquire user input for the password
password_checker(password) # Call the password_checker function with the user's password