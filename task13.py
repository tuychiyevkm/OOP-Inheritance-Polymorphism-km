class Courier:
    def __init__(self, name):
        self.name = name

    def calculate_fee(self):
        pass

class BikeCourier(Courier):
    def calculate_fee(self):
        return f"{self.name}: Fee is $3"

class CarCourier(Courier):
    def calculate_fee(self):
        return f"{self.name}: Fee is $5"

class DroneCourier(Courier):
    def calculate_fee(self):
        return f"{self.name}: Fee is $8 (fastest)"

agents = [BikeCourier("Aziz"), CarCourier("Javlon"), DroneCourier("SkyBot")]
for c in agents:
    print(c.calculate_fee())
