import pytest
import requests


def test_payment_delete(payment_url, auth_headers, create_payment):
    payment_id, _ = create_payment

    delete_url = f"{payment_url}/id/{payment_id}"
    response = requests.delete(delete_url, headers=auth_headers)

    assert response.status_code == 204
