import getpass


Tries = 3


def password():
    # Check the password and allow up to three attempts.
    global Tries

    print("You have 3 tries")
    user_password = getpass.getpass("Enter your password: ")
    Tries = Tries - 1

    # Continue checking while attempts remain.
    while Tries > 0:
        if user_password == "secret123":
            print("Access granted :)")
            break
        else:
            print("Access denied!", Tries, "more tries left")
            user_password = getpass.getpass("Enter your password: ")
            Tries = Tries - 1


password()
