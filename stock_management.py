class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity
        print(f"{quantity} units of {self.name} added to stock.")

    def remove_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            print(f"{quantity} units of {self.name} removed from stock.")
        else:
            print(f"Not enough {self.name} in stock.")

    def check_stock(self):
        print(f"{self.name} stock: {self.quantity} units.")

# creating instances of the Stock class for different products
product1 = Stock("Apple", 50)
product2 = Stock("Banana", 40)
product3 = Stock("Orange", 60)

# adding stock
product1.add_stock(10)
product2.add_stock(20)

# removing stock
product3.remove_stock(30)
product2.remove_stock(50)

# checking stock
product1.check_stock()
product2.check_stock()
product3.check_stock()

