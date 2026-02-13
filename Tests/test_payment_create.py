import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_payment_create(payment_url, auth_headers):
    payload = {
        "amount": 23,
        "customerId": 1,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 2
    }

    response = requests.post(payment_url, json=payload, headers=auth_headers)
    assert response.status_code == 201

    assert response.json()["customerId"] == 1
    assert response.json()["amount"] == 23
    assert "id" in response.json()

    logger.info(
        f"Created new payment with ID: {response.json()['id']}, for Customer ID: {response.json()['customerId']} and price: {response.json()['amount']}"
    )
