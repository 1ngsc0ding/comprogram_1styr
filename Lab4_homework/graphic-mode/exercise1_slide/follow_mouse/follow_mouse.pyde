x = 300


def setup():
    size(600, 400)


def draw():
    background(255)

    draw_balloon(x, 200, 50)

    d = cal_distance(x, 200, mouseX, mouseY)

    if mouseX > x:
        line(x, 200, x + d, 200)
    else:
        line(x, 200, x - d, 200)


def draw_balloon(x, y, size):
    ellipse(x, y, size, size)


def cal_distance(x1, y1, x2, y2):
    diffx = abs(x1 - x2)
    diffy = abs(y1 - y2)

    result = sqrt(diffx * diffx + diffy * diffy)

    return result
