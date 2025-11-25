class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit negative amount: {amount}")
        self.balance += amount
        print(f"[Bank] Deposited {amount}. New balance of '{self.name}': {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot withdraw negative amount: {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient balance in '{self.name}'. Current balance: {self.balance}")
        self.balance -= amount
        print(f"[Bank] Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, amount, target):
        if not isinstance(target, Account):
            raise TypeError("Target must be another Account.")
        self.withdraw(amount)
        target.deposit(amount)
        print(f"[Bank] Transferred {amount} from '{self.name}' to '{target.name}'.")

    def compute_interest(self, rate):
        interest = self.balance * rate
        self.balance += interest
        print(f"[Bank] Applied interest ({rate*100:.1f}%). New balance: {self.balance}")

    def show_balance(self):
        print(f"[Bank] Account '{self.name}' balance: {self.balance}")
