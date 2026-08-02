# Store the x position
x = 0

def setup():
    # Create a 500 x 500 canvas
    size(500, 500)

def draw():
    global x

    # Clear the previous frame
    background(255)

    # Draw the moving ball
    ellipse(x, 250, 80, 80)

    # Move the ball to the right
    x += 2

    # Move back to the left when it leaves the screen
    if x > width + 40:
        x = -40