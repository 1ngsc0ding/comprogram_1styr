import random

def setup():
    size(500, 500)


# Compare each generated radius with this value.
value = 10


def draw_circle(x, y, r):
    ellipse(x, y, r, r)


def draw_rain_drops_until_r_below(value):
    r_flag = True

    # Continue drawing while the flag remains True.
    while r_flag == True:
        x = random.randint(100, 400)
        y = random.randint(150, 350)
        r = random.randint(3, 30)
        draw_circle(x, y, r)

        # Stop when the generated radius is lower than the target value.
        if r < value:
            r_flag = False


def draw():
    background(125)
    draw_rain_drops_until_r_below(value)
