class myQueue:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

q1 = myQueue()
q1.add(10)
q1.add(20)
q1.add(30)
q1.show()

print("Remove:", q1.remove())
q1.show()