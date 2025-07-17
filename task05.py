class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        return f"{self.brand} TV is now ON"

    def turn_off(self):
        return f"{self.brand} TV is OFF"

class Fridge(Appliance):
    def turn_on(self):
        return f"{self.brand} Fridge is cooling"

    def turn_off(self):
        return f"{self.brand} Fridge is OFF"

apps = [TV("LG"), Fridge("Samsung")]
for a in apps:
    print(a.turn_on(), "|", a.turn_off())
