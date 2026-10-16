balloons = [[100, 400, 40, 60], [200, 300, 50, 70], [300, 450, 45, 65], [400, 350, 55, 75], [500, 250, 40, 60]]

def setup():
    size(600, 600)

def draw_balloon(x, y, w, h):
    fill(255, 100, 150)
    ellipse(x, y, w, h)
    stroke(0)
    line(x, y + h / 2, x, y + h / 2 + 40)

def draw():
    background(220)
    
    for balloon in balloons:
        x = balloon[0]
        y = balloon[1]
        w = balloon[2]
        h = balloon[3]
        draw_balloon(x, y, w, h)
        balloon[1] -= 1
        if balloon[1] < -h:
            balloon[1] = height
