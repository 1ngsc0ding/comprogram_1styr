# Draw the letter L
def draw_L(x, y, w, h):
    # Draw the left vertical line
    line(x, y, x, y+h)

    # Draw the bottom horizontal line
    line(x, y+h, x+w, y+h)


# Draw the letter I
def draw_I(x, y, w, h):
    # x = x + w + gap

    # Draw the top horizontal line
    line(x, y, x+w, y)

    # Draw the middle vertical line
    line(x+w/2, y, x+w/2, y+h)

    # Draw the bottom horizontal line
    line(x, y+h, x+w, y+h)


# Draw the letter N
def draw_N(x, y, w, h):
    # x = x + w

    # Draw the left vertical line
    line(x, y, x, y+h)

    # Draw the diagonal line
    line(x, y, x+w, y+h)

    # Draw the right vertical line
    line(x+w, y, x+w, y+h)


# Draw the letter E
def draw_E(x, y, w, h):
    # x = x + w

    # Draw the top horizontal line
    line(x, y, x+w, y)

    # Draw the middle horizontal line
    line(x, y+h/2, x+w, y+h/2)

    # Draw the bottom horizontal line
    line(x, y+h, x+w, y+h)

    # Draw the left vertical line
    line(x, y, x, y+h)


def setup():
    # Create a 600 × 300 canvas
    size(600, 300)

    # Set the space between each letter
    gap = 80

    # Draw the word "LINE"
    draw_L(50, 80, 60, 120)
    draw_I(50 + 60 + gap, 70, 60, 120)
    draw_N(50 + (60 + gap) * 2, 70, 60, 120)
    draw_E(50 + (60 + gap) * 3, 70, 60, 120)