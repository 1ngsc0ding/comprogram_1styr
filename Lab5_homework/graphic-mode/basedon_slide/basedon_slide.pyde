x = 100
speed = 3

def setup():
    size(600, 400)

def draw():
    global x, speed

    background(255)

    ellipse(x, 200, 80, 80)

    x = x + speed

    if x >= 560 or x <= 40:
        speed = speed * -1
