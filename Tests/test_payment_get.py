import pytest
import requests
from configuration import base_url, payment_endpoint


def test_payment_get():
    url = f"{base_url}{payment_endpoint}"

    response = requests.get(url)

    assert response.status_code == 200
