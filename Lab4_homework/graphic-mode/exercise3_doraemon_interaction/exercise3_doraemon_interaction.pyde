import random

# Initial position
doraemon_x = random.randint(300, 700)
doraemon_y = random.randint(300, 700)


def setup():
    size(1000, 1000)
    strokeWeight(4)


def draw():
    background(240, 240, 255)

    draw_doraemon(doraemon_x, doraemon_y)


def draw_doraemon(x, y):
    draw_head(x, y)
    draw_face(x, y)
    draw_eyes(x, y)
    draw_nose(x, y)
    draw_whiskers(x, y)
    draw_mouth(x, y)
    draw_collar(x, y)
    draw_bell(x, y)


def draw_head(x, y):
    fill(0, 150, 255)
    ellipse(x, y, 520, 520)


def draw_face(x, y):
    fill(255)
    ellipse(x, y + 80, 420, 360)


def draw_eyes(x, y):
    fill(255)
    ellipse(x - 45, y - 110, 110, 130)
    ellipse(x + 45, y - 110, 110, 130)

    fill(0)
    ellipse(x + 35, y - 100, 20, 35)

    fill(255)
    ellipse(x + 30, y - 110, 8, 12)

    # Left smiling eye
    stroke(0)
    line(x - 70, y - 100, x - 50, y - 120)
    line(x - 50, y - 120, x - 30, y - 100)


def draw_nose(x, y):
    fill(255, 0, 0)
    ellipse(x, y - 30, 60, 60)

    fill(255)
    ellipse(x - 10, y - 45, 18, 18)

    line(x, y, x, y + 170)


def draw_whiskers(x, y):
    stroke(0)

    # Use while instead of for
    i = 0

    while i < 3:
        offset = i * 50

        # Left whiskers
        line(x - 180, y - 20 + offset,
             x - 50, y + 10 + offset)

        # Right whiskers
        line(x + 50, y + 10 + offset,
             x + 180, y - 20 + offset)

        i = i + 1


def draw_mouth(x, y):
    fill(255, 0, 0)
    arc(x, y + 130, 340, 220, 0, PI)

    line(x - 170, y + 130, x + 170, y + 130)

    fill(255, 140, 0)
    ellipse(x, y + 190, 140, 80)


def draw_collar(x, y):
    fill(255, 0, 0)
    arc(x, y + 260, 380, 60, 0, PI)


def draw_bell(x, y):
    fill(255, 220, 0)
    ellipse(x, y + 315, 90, 90)

    stroke(0)
    line(x - 40, y + 315, x + 40, y + 315)
    line(x, y + 315, x, y + 355)

    fill(0)
    ellipse(x, y + 345, 12, 12)


def mousePressed():
    global doraemon_x, doraemon_y

    # Check the distance between mouse and Doraemon
    distance = dist(mouseX, mouseY, doraemon_x, doraemon_y)

    # if - elif - else
    if distance < 260:
        # Click on Doraemon
        doraemon_x = random.randint(300, 700)
        doraemon_y = random.randint(300, 700)

    elif mouseX < doraemon_x:
        # Click on the left side
        doraemon_x = doraemon_x + 50

    else:
        # Click on the right side
        doraemon_x = doraemon_x - 50
