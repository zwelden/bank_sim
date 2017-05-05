class BankAccount:

    def __init__(self, initial_dep=0, f_name="", l_name="", phone="", address="", account_no=0):
        self.balance = initial_dep
        self.first_name = f_name
        self.last_name = l_name
        self.phone_number = phone
        self.address = address
        self.account_number = account_no
        self.transactions = 0
        self.transactions_record = {}

    def deposit(self, dep_amount):
        if dep_amount > 0:
            self.balance += dep_amount
            self.transactions += 1
            self.transactions_record[self.transactions] = ("D", dep_amount)

        else:
            raise ValueError("deposit amount must be greater than 0")

    def withdrawl(self, wd_amount):
        if wd_amount > 0:
            if wd_amount <= self.balance:
                self.balance -= wd_amount
                self.transactions += 1
                self.transactions_record[self.transactions] = ("W", wd_amount)
            else:
                raise ValueError("The amount to withdrawl is greater than the current ballance")
        else:
            raise ValueError("withdrawl amount must be greater than 0")

    def get_balance(self):
        return self.balance

    def set_account_number(self, account_no):
        if self.account_number == 0:
            self.account_number = account_no
        else:
            raise AttributeError("Bank Account already has an account number assined")

    def get_account_number(self):
        return self.account_number

    def set_account_holder_info(self, f_name, l_name, phone_num, address):
        self.first_name = f_name
        self.last_name = l_name
        self.phone_number = phone_num
        self.address = address

    def get_account_holder_info(self):
        account_num = "Account Number: {0}".format(self.account_number)
        name = "Name: {0} {1}".format(self.first_name, self.last_name)
        ph_num = "Phone Number: {0}".format(self.phone_number)
        address = "Address: {0}".format(self.address)
        account_holder_info = "{0}\n{1}\n{2}\n{3}".format(account_num, name, ph_num, address)
        return account_holder_info

    def get_account_status(self):
        account_num = "Account Number: {0}".format(self.account_number)
        bal = "Balance: {0}".format(self.balance)

    def get_transactions(self):
        if self.transactions > 0:
            transactions_keys = list(self.transactions_record.keys())
            transactions_keys.sort()
            transactions_string = ""
            if self.transactions < 10:
                for key in transactions_keys:
                    tran_type = self.transactions_record[key][0]
                    amount = self.transactions_record[key][1]
                    transactions_string += "Transaction No.: {0}  Type: {1}   Amount: {2}\n".format(key, tran_type, amount)
            else:
                for i in range(1, 11):
                    tran_type = self.transactions_record[i][0]
                    amount = self.transactions_record[i][1]
                    transactions_string += "Transaction No.: {0}  Type: {1}   Amount: {2}\n".format(key, tran_type, amount)
            return transactions_string
        else:
            return "No transactions to report on account"
