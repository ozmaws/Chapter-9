#Account class
class Account(object):
    RATE = 0.02
    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
    def __str__(self):
        result =  "Name:    %s\n" %(self.name)
        result += "PIN:     %s\n" %(self.pin) 
        result += "Balance: %s\n" %(str(self.balance))
        return result
    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name
    def get_pin(self):
        return self.pin
    def deposit(self, amount):
        self.balance += amount
        return None
    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None
    def compute_interest(self):
        interest = self.balance * Account.RATE
        self.deposit(interest)
        return interest
    def __lt__(self, other):
        return self.name < other.name
    def __gt__(self, other):
        return not (self.name == other.name or self.name < other.name)
    def __le__(self, other):
        return self.name == other.name or self.name < other.name
    def __ge__(self, other):
        return self.name == other.name or self.name > other.name
    def __eq__(self, other):
        if self.name is other.name: 
            return True
        elif type(self.name) != type(other.name):
            return False
        else:
            return self.name == other.name
