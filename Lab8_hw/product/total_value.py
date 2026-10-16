class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def show(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

def read_product():
    products = []
    with open("product.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            product = Product(data[0], data[1], data[2])
            products.append(product)
    return products

def show_most_quantity(products):
    most = products[0]
    for product in products:
        if product.quantity > most.quantity:
            most = product
    most.show()

    total = most.price * most.quantity
    print("Total value:", total)

products = read_product()

show_most_quantity(products)