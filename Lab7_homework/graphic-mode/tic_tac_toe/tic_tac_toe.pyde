board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

turn = "X"
game_over = False
message = ""


def setup():
    size(450, 550)
    textAlign(CENTER, CENTER)


def draw():
    background(245)

    fill(40)
    textSize(30)
    text("XO GAME", 225, 40)

    fill(80)
    textSize(20)

    if game_over:
        text(message, 225, 80)
    else:
        text("Turn: " + turn, 225, 80)

    draw_board()

    fill(80)
    textSize(16)
    text("Press R to restart", 225, 490)


def draw_board():
    i = 0

    while i < 3:
        j = 0

        while j < 3:
            x = 75 + j * 100
            y = 120 + i * 100

            fill(255)
            stroke(50)
            strokeWeight(2)
            rect(x, y, 100, 100)

            fill(40)
            textSize(40)
            text(board[i][j], x + 50, y + 50)

            j += 1

        i += 1


def mousePressed():
    global turn
    global game_over
    global message

    if game_over:
        return

    col = int((mouseX - 75) / 100)
    row = int((mouseY - 120) / 100)

    if row >= 0 and row < 3:
        if col >= 0 and col < 3:

            if board[row][col] == "":
                board[row][col] = turn

                if check_win(turn):
                    message = turn + " wins!"
                    game_over = True

                elif check_draw():
                    message = "Draw!"
                    game_over = True

                else:
                    if turn == "X":
                        turn = "O"
                    else:
                        turn = "X"


def check_win(player):
    i = 0

    # rows
    while i < 3:
        if board[i][0] == player:
            if board[i][1] == player:
                if board[i][2] == player:
                    return True
        i += 1

    # columns
    i = 0

    while i < 3:
        if board[0][i] == player:
            if board[1][i] == player:
                if board[2][i] == player:
                    return True
        i += 1

    # diagonals
    if board[0][0] == player:
        if board[1][1] == player:
            if board[2][2] == player:
                return True

    if board[0][2] == player:
        if board[1][1] == player:
            if board[2][0] == player:
                return True

    return False


def check_draw():
    i = 0

    while i < 3:
        j = 0

        while j < 3:

            if board[i][j] == "":
                return False

            j += 1

        i += 1

    return True


def keyPressed():
    global board
    global turn
    global game_over
    global message

    if key == "r" or key == "R":
        board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        turn = "X"
        game_over = False
        message = ""
