class Account:
    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return f"Amount exceeded balance"

    def info(self):
        name = self.name
        id = self.id
        balance = self.balance
        return f"User {name} with account {id} has {balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

