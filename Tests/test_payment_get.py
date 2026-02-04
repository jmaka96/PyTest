import pytest
import requests


def test_payment_get():
    base_url = "http://moderntester.pl:8811/api"
    url = f"{base_url}/payment"

    response = requests.get(url)

    assert response.status_code == 200
