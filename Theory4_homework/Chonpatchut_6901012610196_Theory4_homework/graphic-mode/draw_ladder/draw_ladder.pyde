def setup():
    size(500, 500)


x = 100
y = 100
s = 300


def draw_ladder(x, y, s):
    # Draw the left and right sides of the ladder.
    line(x, y, x, y + s)
    line(x + s, y, x + s, y + s)

    # Draw one rung at a random vertical position.
    y = random(125, 375)
    line(x, y, x + s, y)


def draw():
    draw_ladder(x, y, s)
