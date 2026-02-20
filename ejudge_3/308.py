class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")


balance, withdraw_amount = map(int, input().split())
acc = Account(balance)
acc.withdraw(withdraw_amount)
