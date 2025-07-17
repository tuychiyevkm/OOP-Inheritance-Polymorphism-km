class BankAccount:
    def __init__(self, owner):
        self.owner = owner

    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self):
        return f"{self.owner}: Withdrawal with limits"

class CheckingAccount(BankAccount):
    def withdraw(self):
        return f"{self.owner}: Instant withdrawal allowed"

accounts = [SavingsAccount("Dilshod"), CheckingAccount("Malika")]
for acc in accounts:
    print(acc.withdraw())
