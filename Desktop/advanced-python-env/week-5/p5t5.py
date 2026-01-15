class BankAccount:
    def __init__(self, name, money=0):
        self.__name = name
        self.__balance = money

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
        else:
            print("Deposit must be positive")

    def withdraw(self, amt):
        if amt > self.__balance:
            print("Not enough money")
        elif amt <= 0:
            print("Withdrawal must be positive")
        else:
            self.__balance -= amt

    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())
