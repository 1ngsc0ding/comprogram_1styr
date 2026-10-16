# Week 03: classes, inheritance, overriding and polymorphism
class Balloon:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self):
        self.y -= 2

    def describe(self):
        return f"Balloon at ({self.x}, {self.y}), radius={self.radius}"

class ExpandingBalloon(Balloon):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.change = 1

    def expand_shrink(self):
        self.radius += self.change
        if self.radius >= 60:
            self.change = -1
        elif self.radius <= 30:
            self.change = 1

    def move(self):  # method override
        self.y -= 3
        self.expand_shrink()

if __name__ == "__main__":
    balloons = [Balloon(100, 300, 40), ExpandingBalloon(200, 300, 35)]
    for balloon in balloons:
        balloon.move()
        print(balloon.describe())
