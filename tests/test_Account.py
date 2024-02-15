import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    @patch('builtins.print')
    def test_deposit_success(self, mock_print):
        self.account.deposit(100.0)
        self.assertEqual(self.account.get_balance(), 100.0)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_deposit_invalid_amount(self, mock_print):
        self.account.deposit(-50)
        self.assertEqual(self.account.get_balance(), 0)
        mock_print.assert_called_with("Invalid amount for deposit!")

    @patch('builtins.print')
    def test_deposit_invalid_input(self, mock_print):
        self.account.deposit("invalid")
        self.assertEqual(self.account.get_balance(), 0)
        mock_print.assert_called_with("Invalid amount for deposit!")

    @patch('builtins.print')
    def test_debit_success(self, mock_print):
        self.account.deposit(100.0)
        self.account.debit(50.0)
        self.assertEqual(self.account.get_balance(), 50.0)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_debit_invalid_amount(self, mock_print):
        self.account.debit(50)
        self.assertEqual(self.account.get_balance(), 0)
        mock_print.assert_called_with("Invalid amount for debit!")

    @patch('builtins.print')
    def test_debit_invalid_input(self, mock_print):
        self.account.debit("invalid")
        self.assertEqual(self.account.get_balance(), 0)
        mock_print.assert_called_with("Invalid amount for debit!")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_dict_to_string_deposit(self):
        history_dict = {"operation_type": "deposit", "status": "success", "amount_of_deposit": 100.0, "total_balance": 100.0}
        result = self.account.dict_to_string(history_dict)
        self.assertEqual(result, 'type: deposit status: success amount: 100.0 balance: 100.0')

    def test_dict_to_string_exchange(self):
        history_dict = {"operation_type": "exchange", "status": "success", "pre_exchange_amount": 50.0,
                        "exchange_amount": 40.0, "currency_from": "USD", "currency_to": "EUR"}
        result = self.account.dict_to_string(history_dict)
        expected_result = 'type: exchange status: success pre exchange amount: 50.0 exchange amount: 40.0 currency from: USD currency to: EUR'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
