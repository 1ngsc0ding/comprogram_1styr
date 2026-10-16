# Processing Python Mode sketch — moving balloon with a boundary reset
x = 100

def setup():
    size(500, 500)

def draw():
    global x
    background(255)
    draw_balloon(x, mouseY)
    x += 3
    if x > width + 50:
        x = -50

def draw_balloon(x, y):
    ellipse(x, y, 100, 100)
    line(x, y + 50, x, y + 200)
