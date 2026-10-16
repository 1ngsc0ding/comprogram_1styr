def check_password():

    correct_password = "1234"

    count = 0
    success = False

    while count < 3:

        password = input("Enter password: ")

        if password == correct_password:
            print("Authentication Successful")
            success = True
            break
        count += 1

    if success == False:
        print("Authentication Failed")

check_password()