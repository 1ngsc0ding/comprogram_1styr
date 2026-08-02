x = 0
y = 0
target = 1
speed = 0.08

points = [
    (0, 0),       # Set the starting point at the centre
    (0, -100),    # Set the top point
    (-140, 0),    # Set the left point
    (0, 100),     # Set the bottom point
    (140, 0)      # Set the right point
]

def setup():
    size(1000, 800) # Create a 1000 x 1000 canvas

def draw():
    global x, y, target

    background(255) # Clear the screen before drawing the next frame

    tx, ty = points[target] # Get the next target position

    x += (tx - x) * speed # Move smoothly towards the target on the x-axis
    y += (ty - y) * speed # Move smoothly towards the target on the y-axis

    if dist(x, y, tx, ty) < 2:
        x = tx
        y = ty

        if target == 4:
            target = 1 # Go back to the top point after reaching the right point
        else:
            target += 1 # Move to the next point

    pushMatrix()
    translate(x, y) # Move the whole cartoon character

    strokeWeight(4) # I think it looks ridiculous with a thin outline, so I made it thicker

    # Head
    fill(0, 150, 255) # Change the fill colour to blue
    ellipse(500, 350, 520, 520) # Draw the blue head using a circle

    # Face
    fill(255) # Change the fill colour to white
    ellipse(500, 430, 420, 360) # Draw the white face using an oval

    # Eyes
    ellipse(455, 240, 110, 130) # Draw the left eye using an oval
    ellipse(545, 240, 110, 130) # Draw the right eye using an oval

    fill(0) # Change the fill colour to black
    ellipse(535, 250, 20, 35) # Draw the right pupil

    fill(255) # Change the fill colour to white
    ellipse(530, 240, 8, 12) # Draw the highlight on the right eye

    # Left eye smile
    line(430, 250, 450, 230) # Draw the first line of the smiling eye
    line(450, 230, 470, 250) # Draw the second line of the smiling eye

    # Nose
    fill(255, 0, 0) # Change the fill colour to red
    ellipse(500, 320, 60, 60) # Draw the red nose using a circle

    fill(255) # Change the fill colour to white
    ellipse(490, 305, 18, 18) # Draw the highlight on the nose

    line(500, 350, 500, 520) # Draw the vertical line from the nose to the mouth

    # Left whiskers
    line(320, 330, 450, 360) # Draw the upper left whisker
    line(300, 410, 450, 410) # Draw the middle left whisker
    line(320, 490, 450, 460) # Draw the lower left whisker

    # Right whiskers
    line(550, 360, 680, 330) # Draw the upper right whisker
    line(550, 410, 700, 410) # Draw the middle right whisker
    line(550, 460, 680, 490) # Draw the lower right whisker

    # Mouth
    fill(255, 0, 0) # Change the fill colour to red
    arc(500, 480, 340, 220, 0, PI) # Draw the smiling mouth using a half oval
    line(330, 480, 670, 480) # Draw the top line of the mouth

    # Tongue
    fill(255, 140, 0) # Change the fill colour to orange
    ellipse(500, 540, 140, 80) # Draw the tongue using an oval

    # Collar
    fill(255, 0, 0) # Change the fill colour to red
    arc(500, 610, 380, 60, 0, PI) # Draw the collar using a half oval

    # Bell
    fill(255, 220, 0) # Change the fill colour to yellow
    ellipse(500, 665, 90, 90) # Draw the bell using a circle

    stroke(0) # Change the outline colour to black
    line(460, 665, 540, 665) # Draw the horizontal line on the bell
    line(500, 665, 500, 705) # Draw the vertical line on the bell

    fill(0) # Change the fill colour to black
    ellipse(500, 695, 12, 12) # Draw the small black hole on the bell

    popMatrix()
