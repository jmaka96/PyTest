import pytest
import random
from datetime import datetime, timedelta


@pytest.fixture
def payment_payload():
    return {
        "amount": random.randint(1, 100),
        "customerId": random.randint(1, 20),
        "paymentDate": (datetime(2020, 1, 1) + timedelta(seconds=random.randint(0, 365 * 6 * 86400))).strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"),
        "rentalId": random.randint(1, 50),
        "staffId": random.randint(1, 5)
    }


PAYMENT_PAYLOADS_PARAMS = [
    {
        "amount": 25,
        "customerId": 3,
        "paymentDate": "2022-06-15T10:30:00.000Z",
        "rentalId": 7,
        "staffId": 1
    },
    {
        "amount": 99,
        "customerId": 17,
        "paymentDate": "2024-11-01T08:00:00.000Z",
        "rentalId": 42,
        "staffId": 4
    },
]
