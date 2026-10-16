# Standard Python version of the class example (no graphics dependency)
class Balloon:
    def __init__(self, x, y, radius):
        self.x, self.y, self.radius = x, y, radius

    def move(self):
        self.y -= 2

    def __str__(self):
        return f"Balloon(x={self.x}, y={self.y}, radius={self.radius})"

if __name__ == "__main__":
    balloons = [Balloon(200, 500, 35), Balloon(400, 450, 45)]
    for step in range(3):
        print(f"Step {step + 1}")
        for balloon in balloons:
            balloon.move()
            print(balloon)
