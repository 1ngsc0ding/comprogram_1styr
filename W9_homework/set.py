class mySet:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

s1 = mySet()
s1.add(10)
s1.add(20)
s1.add(10)
s1.show()

s1.remove(10)
s1.show()