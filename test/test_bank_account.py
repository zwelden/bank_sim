import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.basic_bank_account = BankAccount()

    def test_basic_bank_account_opening_value_is_zero_dollars(self):
        self.assertEqual(self.basic_bank_account.balance, 0)

    def test_new_bank_account_opening_balance_is_100_dollars(self):
        new_bank_account_w_100_dollars = BankAccount(100)
        self.assertEqual(new_bank_account_w_100_dollars.balance, 100)

    def test_depoit_to_basic_bank_account_50_dollars(self):
        self.basic_bank_account.deposit(50.00)
        self.assertEqual(self.basic_bank_account.balance, 50)

    def test_deposit_to_basic_bank_account_a_negative_ammount(self):
        self.assertRaises(ValueError, self.basic_bank_account.deposit, -50)

    def test_withdrawl_25_dollars_from_basic_bank_account(self):
        self.basic_bank_account.deposit(50.00)
        starting_balance = self.basic_bank_account.balance
        self.basic_bank_account.withdrawl(25)
        self.assertEqual(self.basic_bank_account.balance, starting_balance-25)

    def test_withdrawl_a_negative_amount_from_basic_account(self):
        self.assertRaises(ValueError, self.basic_bank_account.withdrawl, -20)

    def test_withdrawl_an_amount_that_makes_account_go_negative(self):
        self.assertRaises(ValueError, self.basic_bank_account.withdrawl, 2000)

    def test_get_balance_from_bank_account(self):
        bank_account = BankAccount(100)
        bank_account.deposit(25.75)
        bank_account.withdrawl(5.24)
        self.assertEqual(bank_account.get_balance(), 120.51)
