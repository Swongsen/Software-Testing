import a1web
import pytest
from unittest.mock import Mock

from a1web import run, api_requests, api_shortestDistance, api_bmi

def test_run():
    mock = Mock()
    mock.run()
    mock.run.assert_called()

def test_api_requests():
    mock = Mock()
    mock.api_requests()
    mock.api_requests.assert_called()

def test_api_shortestDistance():
    mock = Mock()
    mock.api_shortestDistance()
    mock.api_shortestDistance.assert_called()

def test_api_bmi():
    mock = Mock()
    mock.api_bmi()
    mock.api_bmi.assert_called()
