class ATM:
    def __init__(self, currency, balance=0):
        self.balance = balance
        self.currency = currency

    def show_currency(self):
        if (self.currency == 'us'):
            return '$'
        elif (self.currency == 'in'):
            return "rbr"

    def check_balance(self):
        print(f"Balance: {self.show_currency()}{self.balance}")

    def withdrawl(self, amount):
        print(f"You just withdrawled {self.show_currency()}{amount}")
        print(
            f"Your new balance is {self.show_currency()}{self.balance - amount}")
        self.balance = self.balance - amount

    def deposit(self, amount):
        print(f"you just deposited {self.show_currency()}{amount}")
        print(
            f"Your new balance is {self.show_currency()}{self.balance + amount}")
        self.balance = self.balance + amount
