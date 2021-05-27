class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount < 0:
            print("Balance can't lower 0")
        else:
            self._balance = amount


bank_account1 = BankAccount(100)
print(bank_account1.get_balance())
bank_account1.set_balance(1000)
print(bank_account1.get_balance())
bank_account1.set_balance(-10000)
print(bank_account1.get_balance())

