import a1web
import pytest
import unittest

from a1web import run, api_requests, api_shortestDistance

class btest(unittest.TestCase):
    def test_run(self):
        response = run()
        self.assertEqual(response.status_code, 200)

    def test_api_requests(self):
        response = api_requests()
        self.assertEqual(response.status_code, 200)

    def test_api_shortestDistance(self):
        response = api_shortestDistance()
        self.assertEqual(response.status_code, 200)

    def test_api_bmi(self):
        response = api_bmi()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
