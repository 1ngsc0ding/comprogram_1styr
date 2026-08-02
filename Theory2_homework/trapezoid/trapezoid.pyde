# จงเขียนโปรแกรมและกำหนดค่าแล้วาดภาพพื้นที่สี่เหลี่ยมคางหมู

# Create a function to draw a trapezoid
def draw_trapezoid(center_x, top_y, top_width, bottom_width, trapezoid_height):

    # Calculate the x-coordinate of the top-left corner
    top_left_x = center_x - top_width / 2

    # Calculate the x-coordinate of the top-right corner
    top_right_x = center_x + top_width / 2

    # Calculate the x-coordinate of the bottom-left corner
    bottom_left_x = center_x - bottom_width / 2

    # Calculate the x-coordinate of the bottom-right corner
    bottom_right_x = center_x + bottom_width / 2

    # Calculate the y-coordinate of the bottom side
    bottom_y = top_y + trapezoid_height

    # Draw the trapezoid using its four corner points
    quad(
        top_left_x, top_y,         # top-left corner
        top_right_x, top_y,        # top-right corner
        bottom_right_x, bottom_y,  # bottom-right corner
        bottom_left_x, bottom_y    # bottom-left corner
    )


# Create a 600 × 400 canvas
size(600, 400)

# Paint the background white
background(255)

# Fill the shape with black
fill(0)

# Draw the outline in black
stroke(0)

# Adjust the outline slightly thicker
strokeWeight(2)

# Draw the trapezoid
draw_trapezoid(
    center_x=300,             # horizontal centre of the trapezoid
    top_y=100,                # y position of the top edge
    top_width=140,            # width of the top edge
    bottom_width=240,         # width of the bottom edge
    trapezoid_height=160      # height of the trapezoid
)
