import pytest
import requests
import random
import string

@pytest.fixture(scope="session")
def base_api_url():
    return "https://api.realworld.io/api"

@pytest.fixture(scope="function")
def test_user():
    return {
        "email": "testuser@example.com",
        "password": "testpassword"
    }

@pytest.fixture(scope="function")
def auth_token(base_api_url, test_user):
    resp = requests.post(f"{base_api_url}/users/login", json={"user": test_user})
    assert resp.status_code == 200
    return resp.json()["user"]["token"]

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
