class Product:
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        pass

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name}: Shipped to your address"

class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name}: Instant download"

products = [PhysicalProduct("Laptop"), DigitalProduct("Ebook")]
for p in products:
    print(p.get_delivery_method())
