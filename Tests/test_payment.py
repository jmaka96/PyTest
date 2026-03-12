import requests
import logging
import pytest
from configuration import base_url, payment_endpoint, headers
from conftest import PAYMENT_PAYLOADS_PARAMS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

payment_url = f"{base_url}{payment_endpoint}"
payment_id = 0


def test_create_payment(payment_payload):
    global payment_id
    response = requests.post(payment_url, json=payment_payload, headers=headers)

    assert response.status_code == 201
    assert response.json()["customerId"] == payment_payload["customerId"]
    assert response.json()["amount"] == payment_payload["amount"]
    assert "id" in response.json()

    payment_id = response.json()["id"]
    logger.info(
        f"Created payment with ID: {payment_id} "
        f"Customer ID: {response.json()['customerId']} "
        f"Amount: {response.json()['amount']}"
    )


def test_get_payments():
    response = requests.get(payment_url)

    assert response.status_code == 200
    logger.info("GET returned status code 200 successfully")


def test_edit_payment(payment_payload):
    assert payment_id is not 0, "Payment ID is not set - test_create_payment failed"

    update_payload = {
        **payment_payload,
        "id": payment_id,
        "amount": 12,
        "customerId": 2,
        "staffId": 3
    }

    response = requests.put(payment_url, json=update_payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["amount"] == 12
    assert response.json()["customerId"] == 2
    assert response.json()["staffId"] == 3
    logger.info(f"Updated payment with ID: {payment_id}")


def test_delete_payment():
    assert payment_id is not 0, "Payment ID is not set - test_create_payment failed"

    response = requests.delete(f"{payment_url}/id/{payment_id}", headers=headers)

    assert response.status_code == 204
    logger.info(f"Deleted payment with ID: {payment_id}")


@pytest.mark.parametrize("payload", PAYMENT_PAYLOADS_PARAMS)
def test_create_payment_parametrized(payload):
    response = requests.post(payment_url, json=payload, headers=headers)

    assert response.status_code == 201
    assert response.json()["customerId"] == payload["customerId"]
    assert response.json()["amount"] == payload["amount"]
    assert "id" in response.json()
    logger.info(
        f"Created payment with ID: {response.json()['id']} "
        f"Customer ID: {response.json()['customerId']} "
        f"Amount: {response.json()['amount']}"
    )


@pytest.mark.parametrize("payload", PAYMENT_PAYLOADS_PARAMS)
def test_edit_payment_parametrized(payload):
    create_response = requests.post(payment_url, json=payload, headers=headers)
    assert create_response.status_code == 201
    created_id = create_response.json()["id"]

    update_payload = {
        **payload,
        "id": created_id,
        "amount": 12,
        "customerId": 2,
        "staffId": 3
    }

    response = requests.put(payment_url, json=update_payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["amount"] == 12
    assert response.json()["customerId"] == 2
    assert response.json()["staffId"] == 3
    logger.info(f"Updated payment with ID: {created_id}")
