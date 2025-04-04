import pytest
import requests

from config import BASE_URL
from payloads.api_payloads import create_user_payload


@pytest.fixture
def create_test_user():
    response = requests.post(f"{BASE_URL}/users", json=create_user_payload)
    assert response.status_code == 201, "Не удалось создать пользователя"
    user_data = response.json()
    return user_data
