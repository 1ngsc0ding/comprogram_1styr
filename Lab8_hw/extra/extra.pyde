
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.speed = 5
        self.score = 0

    def show(self):
        fill(100, 150, 255)
        noStroke()
        ellipse(self.x, self.y, self.size, self.size)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

        self.x = constrain(
            self.x, self.size / 2, width - self.size / 2
        )
        self.y = constrain(
            self.y, self.size / 2, height - self.size / 2
        )


class Coin:
    def __init__(self):
        self.size = 20
        self.reset()

    def reset(self):
        self.x = random(self.size, width - self.size)
        self.y = random(self.size, height - self.size)

    def show(self):
        fill(255, 200, 0)
        stroke(200, 150, 0)
        ellipse(self.x, self.y, self.size, self.size)

    def collect(self, player):
        distance = dist(
            self.x, self.y, player.x, player.y
        )

        if distance < (self.size + player.size) / 2:
            player.score += 1
            self.reset()


player = None
coins = []


def setup():
    global player, coins

    size(600, 600)

    player = Player(width / 2, height / 2)

    coins = [
        Coin(),
        Coin(),
        Coin(),
        Coin(),
        Coin()
    ]


def draw():
    background(240)

    player.show()

    for coin in coins:
        coin.show()
        coin.collect(player)

    fill(0)
    textSize(20)
    text("Score: " + str(player.score), 20, 30)


def keyPressed():
    if keyCode == LEFT:
        player.move(-1, 0)

    elif keyCode == RIGHT:
        player.move(1, 0)

    elif keyCode == UP:
        player.move(0, -1)

    elif keyCode == DOWN:
        player.move(0, 1)
