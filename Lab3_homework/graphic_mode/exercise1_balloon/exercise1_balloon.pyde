# Global variable
x = 100

def setup():
    size(500, 500)
    frameRate(30)

# Draw a circle with radius r
def draw_circle(x, y, r):
    ellipse(x, y, r * 2, r * 2)

# Draw a balloon
def draw_balloon(x, y, r):
    draw_circle(x, y, r)
    line(x, y + r, x, y + r * 4)

# Calculate distance between two points
def cal_distance(x1, y1, x2, y2):
    diffx = abs(x1 - x2)
    diffy = abs(y1 - y2)
    result = sqrt(diffx * diffx + diffy * diffy)
    return result

def draw():
    global x

    background(255)

    # Draw moving balloon
    draw_balloon(x, 200, 50)

    # Calculate distance from balloon to mouse
    d = cal_distance(x, 200, mouseX, mouseY)

    # Draw the line on the same side as the mouse
    if mouseX > x:
        line(x, 200, x + d, 200)
    else:
        line(x, 200, x - d, 200)

    # Move balloon
    x = x + 10

    # Wrap around when reaching the right edge
    if x > width:
        x = 100
