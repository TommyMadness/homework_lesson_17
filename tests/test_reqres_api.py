import requests
import pytest
from jsonschema import validate

from schemas.api_schemas import (
    user_schema,
    register_schema,
    create_user_response_schema,
    update_user_response_schema,
)

from payloads.api_payloads import (
    create_user_payload,
    update_user_payload,
    register_user_valid,
    register_user_missing_password,
)

BASE_URL = "https://reqres.in/api"


# GET / POST / PUT / DELETE


def test_get_single_user_success():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)


def test_post_create_user_success():
    response = requests.post(f"{BASE_URL}/users", json=create_user_payload)
    assert response.status_code == 201
    validate(instance=response.json(), schema=create_user_response_schema)


def test_put_update_user_success():
    response = requests.put(f"{BASE_URL}/users/2", json=update_user_payload)
    assert response.status_code == 200
    validate(instance=response.json(), schema=update_user_response_schema)


def test_delete_user_success():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
    assert response.text == ""


# Positive/Negative


def test_register_success():
    response = requests.post(f"{BASE_URL}/register", json=register_user_valid)
    assert response.status_code == 200
    validate(instance=response.json(), schema=register_schema)


def test_register_missing_password():
    response = requests.post(
        f"{BASE_URL}/register", json=register_user_missing_password
    )
    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"] == "Missing password"


# Status codes


@pytest.mark.parametrize("user_id, expected_status", [(2, 200), (23, 404)])
def test_get_user_status_codes(user_id, expected_status):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == expected_status


# Schema check


def test_user_data_matches_schema():
    response = requests.get(f"{BASE_URL}/users/2")
    validate(instance=response.json(), schema=user_schema)


# No content in response


def test_delete_user_has_no_content():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
    assert response.text == ""
