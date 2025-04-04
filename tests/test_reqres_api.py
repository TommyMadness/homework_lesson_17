import requests
import pytest
from jsonschema import validate

from config import BASE_URL
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
)


# --- GET / POST / PUT / DELETE ---


def test_get_single_user_success():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)


def test_get_non_existing_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/0")
    assert response.status_code == 404


def test_post_create_user_success():
    response = requests.post(f"{BASE_URL}/users", json=create_user_payload)
    assert response.status_code == 201
    validate(instance=response.json(), schema=create_user_response_schema)


def test_put_update_user_success(create_test_user):
    user_id = create_test_user["id"]

    update_response = requests.put(
        f"{BASE_URL}/users/{user_id}", json=update_user_payload
    )
    assert update_response.status_code == 200
    validate(instance=update_response.json(), schema=update_user_response_schema)


def test_delete_user_success(create_test_user):
    user_id = create_test_user["id"]

    delete_response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert delete_response.status_code == 204
    assert delete_response.text == ""


# --- Positive / Negative ---


def test_register_success():
    response = requests.post(f"{BASE_URL}/register", json=register_user_valid)
    assert response.status_code == 200
    validate(instance=response.json(), schema=register_schema)


@pytest.mark.parametrize(
    "payload, expected_error",
    [
        ({"email": "eve.holt@reqres.in"}, "Missing password"),
        ({"password": "pistol"}, "Missing email or username"),
    ],
)
def test_register_missing_required_fields(payload, expected_error):
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"] == expected_error
