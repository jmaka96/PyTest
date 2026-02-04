import pytest
import requests


def test_payment_edit():
    base_url = "http://moderntester.pl:8811/api"
    url = f"{base_url}/payment/"
    headers = {'content-type': 'application/json'}

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
