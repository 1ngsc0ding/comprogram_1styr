x = 100

def setup():
    size(600, 400)

def draw():
    background(255)

    ellipse(x, 200, 50, 50)

    move_balloon()


def move_balloon():
    global x

    x = x + 10

    if x > 500:
        x = 100
