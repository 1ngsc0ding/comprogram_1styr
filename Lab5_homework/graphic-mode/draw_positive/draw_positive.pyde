square_size = 30
number_of_positive = 5

x_position = [110, 330, 550, 770, 990]
speed = [2, -3, 4, -2, 3]

def setup():
    size(1200, 300)
    rectMode(CENTER)

def draw():
    background(200)

    count = 0

    while count < number_of_positive:
        x = x_position[count]
        y = 150

        distance = dist(mouseX, mouseY, x, y)

        if distance < 100:
            current_size = square_size * 2
        else:
            current_size = square_size

        draw_positive(x, y, current_size)

        x_position[count] = x_position[count] + speed[count]

        if x_position[count] > width - current_size:
            speed[count] = speed[count] * -1

        if x_position[count] < current_size:
            speed[count] = speed[count] * -1
            
        count = count + 1

def draw_square(x, y, size):
    fill(200)
    stroke(100)
    rect(x, y, size, size)

def draw_positive(x, y, size):
    draw_square(x, y, size)
    draw_square(x, y - size, size)
    draw_square(x, y + size, size)
    draw_square(x - size, y, size)
    draw_square(x + size, y, size)
