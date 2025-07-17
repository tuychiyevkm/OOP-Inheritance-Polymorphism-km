class Vehicle:
    def __init__(self, model):
        self.model = model

    def show_info(self):
        pass

class Car(Vehicle):
    def show_info(self):
        return f"{self.model}: 4 wheels, air conditioner"

class Bike(Vehicle):
    def show_info(self):
        return f"{self.model}: 2 wheels, no AC"

vehicles = [Car("Chevrolet"), Bike("Yamaha")]
for v in vehicles:
    print(v.show_info())
