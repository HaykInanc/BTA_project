import unittest
from unittest.mock import patch
from CurrencyExchange import CurrencyExchange

class TestCurrencyExchange(unittest.TestCase):

    def setUp(self):
        self.currency_exchange = CurrencyExchange()

    @patch('FileManager.FileManager.add_to_json')
    @patch('CurrencyExchange.CurrencyExchange.get_exchange_rates')
    def test_exchange_currency_success(self, mock_get_exchange_rates, mock_add_to_json):
        mock_get_exchange_rates.return_value = {'USD': 1.15, 'EUR': 1.0}
        result = self.currency_exchange.exchange_currency('USD', 'EUR', 100.0)
        expected_result = 100.0 / 1.15
        self.assertEqual(result, expected_result)
        mock_add_to_json.assert_called_once()

    @patch('FileManager.FileManager.add_to_json')
    @patch('CurrencyExchange.CurrencyExchange.get_exchange_rates')
    def test_exchange_currency_invalid_currency(self, mock_get_exchange_rates, mock_add_to_json):
        mock_get_exchange_rates.return_value = {'USD': 1.15, 'EUR': 1.0}
        result = self.currency_exchange.exchange_currency('GBP', 'EUR', 100.0)
        self.assertIsNone(result)
        mock_add_to_json.assert_called_once_with(
            {'operation_type': 'exchange', 'status': 'failure', 'pre_exchange_amount': 100.0, 'exchange_amount': None,
             'currency_from': 'GBP', 'currency_to': 'EUR'}, 'hist.json'
        )

    @patch('builtins.print')
    @patch('FileManager.FileManager.add_to_json')
    @patch('CurrencyExchange.CurrencyExchange.get_exchange_rates')
    def test_exchange_currency_invalid_amount(self, mock_get_exchange_rates, mock_add_to_json, mock_print):
        mock_get_exchange_rates.return_value = {'USD': 1.15, 'EUR': 1.0}
        result = self.currency_exchange.exchange_currency('USD', 'EUR', 'invalid')
        self.assertIsNone(result)
        mock_add_to_json.assert_called_once_with(
            {'operation_type': 'exchange', 'status': 'failure', 'pre_exchange_amount': 'invalid', 'exchange_amount': None, 'currency_from': 'USD', 'currency_to': 'EUR'}, 'hist.json'
        )
        mock_print.assert_called_with("Currency exchange failed!")


if __name__ == '__main__':
    unittest.main()
