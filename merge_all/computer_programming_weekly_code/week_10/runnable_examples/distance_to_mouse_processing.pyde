# Processing Python Mode sketch — distance from balloon to mouse
balloon_x = 250
balloon_y = 250

def setup():
    size(600, 500)

def draw():
    background(255)
    draw_balloon(balloon_x, balloon_y, 50)
    distance = calculate_distance(balloon_x, balloon_y, mouseX, mouseY)
    line(balloon_x, balloon_y, mouseX, mouseY)
    fill(0)
    text("Distance: " + str(int(distance)), 10, 20)

def draw_balloon(x, y, radius):
    ellipse(x, y, radius * 2, radius * 2)
    line(x, y + radius, x, y + radius + 80)

def calculate_distance(x1, y1, x2, y2):
    difference_x = x1 - x2
    difference_y = y1 - y2
    return sqrt(difference_x * difference_x + difference_y * difference_y)
