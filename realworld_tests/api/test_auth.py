import pytest
pytestmark = pytest.mark.api

def test_login_invalid(base_api_url):
    resp = requests.post(f"{base_api_url}/users/login", json={
        "user": {"email": "wrong@test.com", "password": "wrongpass"}
    })
    assert resp.status_code == 403 or 422

def test_login_valid(base_api_url, test_user):
    resp = requests.post(f"{base_api_url}/users/login", json={"user": test_user})
    assert resp.status_code == 200
    assert "token" in resp.json()["user"]
