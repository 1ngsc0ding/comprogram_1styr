def setup():
    size(500, 500)


# Receive the target raindrop volume from the user.
volume = float(input("Volume of rain drops per loop: "))


def draw_circle(x, y, r):
    ellipse(x, y, r, r)


def draw_rain_drops_until(volume):
    sum = 0

    # Continue drawing until the accumulated size reaches the target volume.
    while sum < volume:
        x = random(100, 400)
        y = random(150, 350)
        r = random(3, 30)
        draw_circle(x, y, r)
        sum = sum + r


def draw():
    global volume
    background(125)
    draw_rain_drops_until(volume)
