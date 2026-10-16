class myBag:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

b1 = myBag()
b1.add(10)
b1.add(10)
b1.add(20)
b1.show()

b1.remove(10)
b1.show()