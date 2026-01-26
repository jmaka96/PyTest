import pytest
import requests


def test_create_payment():
    base_url = "http://moderntester.pl:8811/api"
    url = f"{base_url}/payment"

    payload = {
        "amount": 23,
        "customerId": 1,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 2
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201

    assert response.json()["customerId"] == 1
    assert response.json()["amount"] == 23
    assert "id" in response.json()

    print(
        f"utworzony nową płatnośc o ID: {response.json()['id']}, dla customera o ID: {response.json()['customerId']} oraz ceną: {response.json()['amount']}")
