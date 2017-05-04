class BankAccount:

    def __init__(self, initial_dep=0, f_name="", l_name="", phone="", address=""):
        self.balance = initial_dep
        self.first_name = f_name
        self.last_name = l_name
        self.phone_number = phone
        self.address = address

    def deposit(self, dep_amount):
        if dep_amount > 0:
            self.balance += dep_amount
        else:
            raise ValueError("deposit amount must be greater than 0")

    def withdrawl(self, wd_amount):
        if wd_amount > 0:
            if wd_amount <= self.balance:
                self.balance -= wd_amount
            else:
                raise ValueError("The amount to withdrawl is greater than the current ballance")
        else:
            raise ValueError("withdrawl amount must be greater than 0")

    def get_balance(self):
        return self.balance
