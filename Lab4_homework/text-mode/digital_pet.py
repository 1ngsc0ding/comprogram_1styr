def show_status(hunger, happiness):
    print("\n========== PET STATUS ==========")
    print("Hunger    :", hunger)
    print("Happiness :", happiness)

    if hunger >= 80:
        print("Your pet is very hungry! Feed it soon!")
    elif happiness <= 20:
        print("Your pet is feeling sad! Play with it soon!")
    else:
        print("Your pet is doing well!")

def feed_pet(hunger):
    hunger = hunger - 20
    if hunger < 0:
        hunger = 0
    print("Your pet has been fed!")
    return hunger

def play_pet(hunger, happiness):
    happiness = happiness + 20
    hunger = hunger + 10
    if happiness > 100:
        happiness = 100
    if hunger > 100:
        hunger = 100
    print("Your pet is happy! You played together.")
    return hunger, happiness

def digital_pet():
    hunger = 50
    happiness = 50
    name = input("What would you like to name your pet?\n")

    print("Welcome to Digital Pet!")
    print(f"Your pet's name is {name}.")

    while True:
        print("\n========== DIGITAL PET ==========")
        print("1. Feed")
        print("2. Play")
        print("3. Check status")
        print("0. Exit")

        choice = int(input("Choose: "))
        if choice == 1:
            hunger = feed_pet(hunger)
        elif choice == 2:
            hunger, happiness = play_pet(
                hunger,
                happiness
            )
        elif choice == 3:
            show_status(hunger, happiness)
        elif choice == 0:
            print(f"Goodbye! Take care of {name}!")
            break
        else:
            print("Invalid choice. Please try again.")

digital_pet()