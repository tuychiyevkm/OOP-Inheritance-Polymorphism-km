class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defend(self):
        pass

class Warrior(Character):
    def attack(self):
        return f"{self.name} slashes with sword"

    def defend(self):
        return f"{self.name} blocks with shield"

class Mage(Character):
    def attack(self):
        return f"{self.name} casts a fireball"

    def defend(self):
        return f"{self.name} uses magic barrier"

class Archer(Character):
    def attack(self):
        return f"{self.name} shoots arrows"

    def defend(self):
        return f"{self.name} dodges swiftly"

players = [Warrior("Thor"), Mage("Merlin"), Archer("Legolas")]
for p in players:
    print(p.attack(), "|", p.defend())
