# Processing Python Mode — draw a row of simple steps
def setup():
    size(600, 400)
    background(255)
    draw_stairs(80, 300, 35)

def draw_stairs(x, y, step_size):
    step = 0
    while step < 6:
        line(x + step * step_size, y - step * step_size,
             x + (step + 1) * step_size, y - step * step_size)
        line(x + (step + 1) * step_size, y - step * step_size,
             x + (step + 1) * step_size, y - (step + 1) * step_size)
        step += 1
