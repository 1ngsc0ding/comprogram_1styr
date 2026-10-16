SIZE = 7

game_map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '.', 'T', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

player_row = 1
player_col = 1

steps = 0
game_over = False


def show_map():
    print("\n" * 2)

    print("==============================")
    print("        TREASURE HUNT")
    print("==============================")

    i = 0

    while i < SIZE:
        j = 0
        line = ""

        while j < SIZE:
            line += game_map[i][j] + " "
            j += 1

        print(line)
        i += 1

    print("------------------------------")
    print("Steps:", steps)
    print("W = Up | S = Down")
    print("A = Left | D = Right")
    print("Q = Quit")
    print("------------------------------")


def move_player(direction):
    global player_row
    global player_col
    global steps
    global game_over

    new_row = player_row
    new_col = player_col

    if direction == "w":
        new_row -= 1
    elif direction == "s":
        new_row += 1
    elif direction == "a":
        new_col -= 1
    elif direction == "d":
        new_col += 1
    else:
        print("Please use W A S D")
        return

    if game_map[new_row][new_col] == "#":
        print("You cannot go through the wall!")
        return

    if game_map[new_row][new_col] == "T":
        game_map[player_row][player_col] = "."
        player_row = new_row
        player_col = new_col
        game_map[player_row][player_col] = "P"

        steps += 1
        game_over = True

        print("\nYou found the treasure!")
        print("You used", steps, "steps.")
        return

    game_map[player_row][player_col] = "."

    player_row = new_row
    player_col = new_col

    game_map[player_row][player_col] = "P"

    steps += 1

while game_over == False:
    show_map()

    command = input("Move: ").lower()

    if command == "q":
        print("\nGame Over!")
        game_over = True
    elif len(command) == 1:
        move_player(command)
    else:
        print("Please enter only one letter.")

print("\nThanks for playing!")
