# Draw a balloon at any position
def draw_balloon(x, y):
    ellipse(x, y, 80, 80)
    line(x, y + 40, x, y + 150)

# Create a 500 x 500 canvas
size(500, 500)

# Draw three balloons
draw_balloon(120, 150)
draw_balloon(250, 220)
draw_balloon(380, 120)