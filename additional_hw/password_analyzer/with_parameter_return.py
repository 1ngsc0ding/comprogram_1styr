def check_password(correct_password):

    count = 0

    while count < 3:
        password = input("Enter password: ")
        if password == correct_password:
            return True
        count += 1
    return False


result = check_password("1234")

if result:
    print("Authentication Successful")
else:
    print("Authentication Failed")