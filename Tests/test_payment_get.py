import pytest
import requests
from configuration import base_url, payment_endpoint


def test_payment_get(payment_url):
    response = requests.get(payment_url)

    assert response.status_code == 200
