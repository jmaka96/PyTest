import pytest
import requests
from configuration import base_url, payment_endpoint, headers


def test_payment_delete():
    payment_id = 16434
    url = f"{base_url}{payment_endpoint}/id/{payment_id}"
    response = requests.delete(url, headers=headers)

    assert response.status_code == 204
