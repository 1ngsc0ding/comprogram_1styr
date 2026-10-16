# Processing Python Mode sketch — paste into a Python Mode sketch in Processing
def setup():
    size(500, 500)
    background(255)
    draw_balloon(200, 200)
    draw_balloon(400, 200)

def draw_balloon(x, y):
    ellipse(x, y, 100, 100)
    line(x, y + 50, x, y + 200)
