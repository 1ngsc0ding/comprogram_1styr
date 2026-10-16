class Matrix:
    def __init__(self, data):
        self.data = data
        self.row = len(data)
        self.col = len(data[0])

    def show(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                value = self.data[i][j] + other.data[i][j]
                row.append(value)
            result.append(row)
        return Matrix(result)

    def subtract(self, other):
        result = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                value = self.data[i][j] - other.data[i][j]
                row.append(value)
            result.append(row)
        return Matrix(result)

    def multiplication(self, other):
        result = []
        for i in range(self.row):
            row = []
            for j in range(other.col):
                value = 0
                for k in range(self.col):
                    value += self.data[i][k] * other.data[k][j]
                row.append(value)
            result.append(row)
        return Matrix(result)

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print("Matrix A")
a.show()

print("Matrix B")
b.show()

print("A + B")
c = a.add(b)
c.show()

print("A - B")
d = a.subtract(b)
d.show()

print("A x B")
e = a.multiplication(b)
e.show()