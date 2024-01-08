import unittest
from unittest.mock import patch, Mock
from app import get_gold_price
import requests

class TestGetGoldPrice(unittest.TestCase):
    @patch('app.requests.get')
    def test_get_gold_price_failed_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"cena": "259.84"}]
        mock_get.return_value = mock_response

        result = get_gold_price("20-12-2023")
        self.assertEqual(result, "Gold price on 20-12-2023: 259.84 PLN per gram")

    @patch('app.requests.get')
    def test_get_gold_price_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"cena": "259.84"}]
        mock_get.return_value = mock_response

        result = get_gold_price("20-12-2023")
        self.assertEqual(result, "Gold price on 2023-12-20: 259.84 PLN per gram")

    @patch('app.requests.get')
    def test_get_gold_price_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_gold_price("20-12-2023")
        self.assertEqual(result, "Failed to retrieve the gold price.")

    @patch('app.requests.get')
    def test_get_gold_price_exception(self, mock_get):
        mock_get.side_effect = requests.RequestException("An error occurred")

        result = get_gold_price("20-12-2023")
        self.assertEqual(result, "An error occurred while fetching the data: An error occurred")
