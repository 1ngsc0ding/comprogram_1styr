def setup():
    size(500, 500)


# Set the number of raindrops drawn in each loop.
n = int(input("Amount of rain drops: "))


def draw_circle(x, y, r):
    ellipse(x, y, r, r)


def draw_rain_drops(n):
    i = 0

    # Draw exactly n raindrops.
    while i < n:
        x = random(100, 400)
        y = random(150, 350)
        r = random(3, 30)
        draw_circle(x, y, r)
        i = i + 1


def draw():
    background(125)
    draw_rain_drops(n)
