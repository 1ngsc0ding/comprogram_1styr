# Processing Python Mode sketch — parallel arrays animation
x_positions = []
y_positions = []
speeds = []
number_of_circles = 12

def setup():
    size(1000, 600)
    for unused in range(number_of_circles):
        x_positions.append(random(100, 900))
        y_positions.append(random(50, 400))
        speeds.append(random(1, 5))

def draw():
    background(255)
    index = 0
    while index < len(x_positions):
        ellipse(x_positions[index], y_positions[index], 20, 20)
        y_positions[index] += speeds[index]
        if y_positions[index] > height + 10:
            y_positions[index] = -10
        index += 1
