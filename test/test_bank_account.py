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

    def test_set_account_holder_info_on_new_account(self):
        new_account = BankAccount(0)
        new_account.set_account_holder_info("Zach", "Welden", "918-555-1234", "123 S Main St, Tulsa, OK, 74123")
        self.assertTrue(new_account.first_name == "Zach")
        self.assertTrue(new_account.last_name == "Welden")
        self.assertTrue(new_account.phone_number == "918-555-1234")
        self.assertTrue(new_account.address == "123 S Main St, Tulsa, OK, 74123")

    def test_get_account_holder_info_after_creating_new_account(self):
        new_account = BankAccount()
        test_account_output_string = "Account Number: 0\nName:  \nPhone Number: \nAddress: "
        self.assertTrue(new_account.get_account_holder_info() == test_account_output_string)

    def test_get_account_holder_info_after_updating_account_number(self):
        new_account = BankAccount()
        new_account.set_account_number(123456789)
        test_account_output_string = "Account Number: 123456789\nName:  \nPhone Number: \nAddress: "
        self.assertTrue(new_account.get_account_holder_info() == test_account_output_string)

    def test_get_account_holder_info_after_updating_account_number_and_account_holder_info(self):
        new_account = BankAccount()
        new_account.set_account_number(123456789)
        new_account.set_account_holder_info("Zach", "Welden", "918-555-1234", "123 S Main St, Tulsa, OK, 74123")
        test_account_output_string = "Account Number: 123456789\nName: Zach Welden\nPhone Number: 918-555-1234\nAddress: 123 S Main St, Tulsa, OK, 74123"

    def test_transactions_report_on_new_account(self):
        new_account = BankAccount()
        self.assertTrue(new_account.get_transactions() == "No transactions to report on account")

    def test_transaction_report_after_8_transactions_dep_and_wd(self):
        new_account = BankAccount()
        new_account.deposit(100)
        new_account.withdrawl(25)
        new_account.deposit(50)
        new_account.withdrawl(75)
        new_account.withdrawl(10)
        new_account.deposit(20)
        new_account.deposit(9)
        new_account.withdrawl(17)
        tsl1 = "Transaction No.: 1  Type: D   Amount: 100\n"
        tsl2 = "Transaction No.: 2  Type: W   Amount: 25\n"
        tsl3 = "Transaction No.: 3  Type: D   Amount: 50\n"
        tsl4 = "Transaction No.: 4  Type: W   Amount: 75\n"
        tsl5 = "Transaction No.: 5  Type: W   Amount: 10\n"
        tsl6 = "Transaction No.: 6  Type: D   Amount: 20\n"
        tsl7 = "Transaction No.: 7  Type: D   Amount: 9\n"
        tsl8 = "Transaction No.: 8  Type: W   Amount: 17\n"
        trans_string = tsl1 + tsl2 + tsl3 + tsl4 + tsl5 + tsl6 + tsl7 + tsl8
        self.assertTrue(new_account.get_transactions() == trans_string)
