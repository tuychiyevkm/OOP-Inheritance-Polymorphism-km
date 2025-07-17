class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_bonus(self):
        pass

class Developer(Employee):
    def calculate_bonus(self):
        return f"{self.name}'s bonus: 20% of salary"

class Manager(Employee):
    def calculate_bonus(self):
        return f"{self.name}'s bonus: 30% of salary"

emps = [Developer("Ali"), Manager("Vali")]
for e in emps:
    print(e.calculate_bonus())