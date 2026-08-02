# Create a 500 x 500 canvas
size(500, 500)

# Set the top-left position
x = 200
y = 100

# Draw the left side
line(x, y, x, y + 200)

# Draw the right side
line(x + 100, y, x + 100, y + 200)

# Calculate the middle position
middle = y + 100

# Draw the middle line
line(x, middle, x + 100, middle)