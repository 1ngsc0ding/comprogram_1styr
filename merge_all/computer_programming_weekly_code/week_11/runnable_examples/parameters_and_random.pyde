# Processing Python Mode sketch — parameters and random positions
def setup():
    size(500, 500)
    background(255)
    draw_balloon(150, 180, 40)
    draw_balloon(350, 180, 60)

def draw_balloon(x, y, radius):
    ellipse(x, y, radius * 2, radius * 2)
    line(x, y + radius, x, y + radius + 100)
