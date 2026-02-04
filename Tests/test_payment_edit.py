import pytest
import requests
from configuration import base_url, payment_endpoint, headers


def test_payment_edit():
    url = f"{base_url}{payment_endpoint}"

    update_payload = {
        "amount": 12,
        "customerId": 2,
        "id": 16434,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 3
    }

    response = requests.put(url, json=update_payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["amount"] == 12
    assert response.json()["customerId"] == 2
    assert response.json()["staffId"] == 3
