import pytest
import requests

def test_payment_delete():
    base_url = "http://moderntester.pl:8811/api"
    payment_id = 16434
    url = f"{base_url}/payment/id/{payment_id}"

    headers = {"Content-Type": "application/json"}
    response = requests.delete(url, headers=headers)

    assert response.status_code == 204