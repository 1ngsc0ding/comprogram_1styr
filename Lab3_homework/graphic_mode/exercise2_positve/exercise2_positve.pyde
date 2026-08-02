x = 0
y = 0
square_size = 60


def setup():
    global x, y

    size(700, 700)
    rectMode(CENTER)

    # Random starting position
    x = random(150, 550)
    y = random(150, 550)


def draw():
    background(255)

    draw_positive(x, y, square_size)


def draw_square(x, y, size):
    fill(120, 180, 255)
    stroke(0)
    rect(x, y, size, size)


def draw_positive(x, y, size):
    draw_square(x, y, size)
    draw_square(x, y - size, size)
    draw_square(x, y + size, size)
    draw_square(x - size, y, size)
    draw_square(x + size, y, size)


def mousePressed():
    global x, y

    # Check if the mouse clicks near the center
    if abs(mouseX - x) <= square_size * 1.5:

        if abs(mouseY - y) <= square_size * 1.5:

            x = random(150, 550)
            y = random(150, 550)
