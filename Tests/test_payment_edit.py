import pytest
import requests


def test_payment_edit(payment_url, auth_headers, create_payment):
    payment_id, _ = create_payment

    update_payload = {
        "amount": 12,
        "customerId": 2,
        "id": payment_id,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 3
    }

    response = requests.put(payment_url, json=update_payload, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["amount"] == 12
    assert response.json()["customerId"] == 2
    assert response.json()["staffId"] == 3
