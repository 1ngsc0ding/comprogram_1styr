# Processing Python Mode sketch — fixed number of random circles
def setup():
    size(500, 500)
    background(255)
    draw_rain_drops(30)

def draw_rain_drops(number):
    count = 0
    while count < number:
        x = random(100, 400)
        y = random(100, 400)
        radius = random(3, 30)
        ellipse(x, y, radius, radius)
        count += 1
