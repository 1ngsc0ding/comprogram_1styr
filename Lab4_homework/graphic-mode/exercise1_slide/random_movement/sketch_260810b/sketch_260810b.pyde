def setup():
    size(500, 500)


def draw():
    background(255)

    x = random(100, 400)
    y = random(150, 350)

    draw_circle(x, y, random(3, 30))


def draw_circle(x, y, r):
    ellipse(x, y, r, r)
