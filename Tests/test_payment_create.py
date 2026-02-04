import pytest
import requests
import logging
from configuration import base_url, payment_endpoint, headers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_payment_create():
    url = f"{base_url}{payment_endpoint}"

    payload = {
        "amount": 23,
        "customerId": 1,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 2
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201

    assert response.json()["customerId"] == 1
    assert response.json()["amount"] == 23
    assert "id" in response.json()

    logger.info(
        f"utworzono nową płatnośc o ID: {response.json()['id']}, dla customera o ID: {response.json()['customerId']} oraz ceną: {response.json()['amount']}"
    )
