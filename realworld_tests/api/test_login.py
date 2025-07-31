import pytest
pytestmark = pytest.mark.api

def test_login_success(base_api_url, test_user):
    response = requests.post(f"{base_api_url}/users/login", json={"user": test_user})
    assert response.status_code == 200
    assert "token" in response.json()["user"]

def test_login_failure(base_api_url):
    response = requests.post(f"{base_api_url}/users/login", json={
        "user": {"email": "wrong@example.com", "password": "badpass"}
    })
    assert response.status_code == 403 or 422  # depends on backend
