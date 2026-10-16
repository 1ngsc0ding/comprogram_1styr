# You can adjust the number of positive right here!
number_of_positive = 5

square_size = 60


def setup():
    size(1200, 300)
    rectMode(CENTER)


def draw():
    background(200)

    x = 110
    count = 0

    # Repeat draw_positive() according to the number above
    while count < number_of_positive:
        draw_positive(x, 150, square_size)

        # Move to the right
        # 220 = 180 pixels for the + itself + 40 pixels of space
        x = x + 220

        # Count the number of positive
        count = count + 1


def draw_square(x, y, size):
    fill(200)
    stroke(100)
    rect(x, y, size, size)


def draw_positive(x, y, size):
    # Center
    draw_square(x, y, size)

    # Top
    draw_square(x, y - size, size)

    # Bottom
    draw_square(x, y + size, size)

    # Left
    draw_square(x - size, y, size)

    # Right
    draw_square(x + size, y, size)
