import pytest
import requests
from configuration import base_url, payment_endpoint, headers


@pytest.fixture
def payment_url():
    return f"{base_url}{payment_endpoint}"


@pytest.fixture
def auth_headers():
    return headers


@pytest.fixture
def create_payment(payment_url, auth_headers):
    payload = {
        "amount": 23,
        "customerId": 1,
        "paymentDate": "2026-01-26T11:53:06.277Z",
        "rentalId": 40,
        "staffId": 2
    }
    response = requests.post(payment_url, json=payload, headers=auth_headers)
    assert response.status_code == 201, f"Failed to create payment: {response.text}"
    payment_data = response.json()
    payment_id = payment_data["id"]

    yield payment_id, payment_data

    delete_url = f"{payment_url}/id/{payment_id}"
    delete_response = requests.delete(delete_url, headers=auth_headers)
    assert delete_response.status_code in (204, 404), f"Failed to delete payment {payment_id}: {delete_response.text}"
