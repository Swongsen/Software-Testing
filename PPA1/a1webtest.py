import a1web
import pytest
import unittest
from unittest.mock import patch
from users import get_users
from a1web import run, api_requests, api_shortestDistance, api_bmi

class btest(unittest.TestCase):
    @patch('users.requests.get')
    def test_run(self, mock_get):
        mock_get.return_value.status_code == 200
        response = get_users()
        self.assertEqual(response.status_code, 200)

    @patch('users.requests.get')
    def test_api_requests(self, mock_get):
        mock_get.return_value.status_code == 200
        response = get_users()
        self.assertEqual(response.status_code, 200)

    @patch('users.requests.get')
    def test_api_shortestDistance(self, mock_get):
        mock_get.return_value.status_code == 200
        response = get_users()
        self.assertEqual(response.status_code, 200)

    @patch('users.requests.get')
    def test_api_bmi(self, mock_get):
        mock_get.return_value.status_code == 200
        response = api_bmi()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
