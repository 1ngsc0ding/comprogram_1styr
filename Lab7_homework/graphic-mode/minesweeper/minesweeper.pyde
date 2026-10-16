SIZE = 8
CELL = 50
MINES = 10

mine = []
number = []
open_cell = []

game_over = False
win = False


def setup():
    size(400, 450)
    textAlign(CENTER, CENTER)
    new_game()


def draw():
    background(240)

    fill(40)
    textSize(28)
    text("MINESWEEPER", 200, 25)

    if game_over:
        fill(180, 0, 0)
        textSize(18)
        text("GAME OVER - Press R to restart", 200, 420)

    elif win:
        fill(0, 130, 0)
        textSize(18)
        text("YOU WIN! - Press R to restart", 200, 420)

    else:
        fill(70)
        textSize(16)
        text("Mines: " + str(MINES), 200, 420)

    draw_board()


def new_game():
    global mine
    global number
    global open_cell
    global game_over
    global win

    mine = []
    number = []
    open_cell = []

    # create 2D arrays
    i = 0
    while i < SIZE:

        mine_row = []
        number_row = []
        open_row = []

        j = 0
        while j < SIZE:
            mine_row.append(False)
            number_row.append(0)
            open_row.append(False)
            j += 1

        mine.append(mine_row)
        number.append(number_row)
        open_cell.append(open_row)

        i += 1

    # put mines
    count = 0

    while count < MINES:
        r = int(random(SIZE))
        c = int(random(SIZE))

        if mine[r][c] == False:
            mine[r][c] = True
            count += 1

    # calculate numbers
    i = 0

    while i < SIZE:
        j = 0

        while j < SIZE:
            if mine[i][j] == False:
                number[i][j] = count_mines(i, j)
            j += 1
        i += 1

    game_over = False
    win = False

def count_mines(row, col):
    count = 0

    i = row - 1
    
    while i <= row + 1:
        j = col - 1
        while j <= col + 1:
            if i >= 0 and i < SIZE:
                if j >= 0 and j < SIZE:
                    if mine[i][j]:
                        count += 1
            j += 1
        i += 1
    return count

def draw_board():
    i = 0

    while i < SIZE:
        j = 0

        while j < SIZE:

            x = j * CELL
            y = i * CELL + 50

            if open_cell[i][j]:
                fill(220)
            else:
                fill(170)

            stroke(80)
            strokeWeight(1)
            rect(x, y, CELL, CELL)
            if open_cell[i][j]:
                if mine[i][j]:
                    fill(30)
                    ellipse(x + 25, y + 25, 25, 25)

                elif number[i][j] > 0:
                    fill(40)
                    textSize(22)
                    text(
                        str(number[i][j]),
                        x + 25,
                        y + 25
                    )
            j += 1
        i += 1


def mousePressed():
    global game_over
    global win

    if game_over or win:
        return

    col = int(mouseX / CELL)
    row = int((mouseY - 50) / CELL)

    if row >= 0 and row < SIZE:
        if col >= 0 and col < SIZE:

            if open_cell[row][col] == False:

                open_cell[row][col] = True

                if mine[row][col]:
                    game_over = True
                    show_all_mines()

                else:
                    check_win()


def show_all_mines():
    i = 0
    while i < SIZE:
        j = 0
        while j < SIZE:
            if mine[i][j]:
                open_cell[i][j] = True
            j += 1
        i += 1


def check_win():
    global win

    safe_cells = 0
    opened_cells = 0

    i = 0

    while i < SIZE:
        j = 0
        while j < SIZE:
            if mine[i][j] == False:
                safe_cells += 1
                if open_cell[i][j]:
                    opened_cells += 1
            j += 1
        i += 1
    if opened_cells == safe_cells:
        win = True


def keyPressed():
    if key == "r" or key == "R":
        new_game()
