class Balloon:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def show(self):
        fill(255, 100, 150)
        ellipse(self.x, self.y, self.w, self.h)
        stroke(0)
        line(self.x, self.y + self.h / 2, self.x, self.y + self.h / 2 + 40)
    def move(self):
        self.y -= 1
        if self.y < -self.h:
            self.y = height

balloons = [Balloon(100, 400, 40, 60), Balloon(200, 300, 50, 70), Balloon(300, 450, 45, 65), Balloon(400, 350, 55, 75), Balloon(500, 250, 40, 60)]

def setup():
    size(600, 600)

def draw():
    background(220)
    for balloon in balloons:
        balloon.show()
        balloon.move()
