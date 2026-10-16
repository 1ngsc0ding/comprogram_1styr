# Processing Python Mode sketch — class/object example
balloons = []

class Balloon:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        ellipse(self.x, self.y, self.radius * 2, self.radius * 2)
        line(self.x, self.y + self.radius, self.x, self.y + self.radius + 100)

    def move(self):
        self.y -= 2
        if self.y < -self.radius:
            self.y = height + self.radius

def setup():
    size(1000, 700)
    balloons.append(Balloon(200, 500, 35))
    balloons.append(Balloon(400, 450, 45))
    balloons.append(Balloon(650, 550, 30))

def draw():
    background(255)
    for balloon in balloons:
        balloon.show()
        balloon.move()
