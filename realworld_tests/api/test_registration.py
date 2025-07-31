import pytest
pytestmark = pytest.mark.api

def test_register_new_user(base_api_url):
    new_user = {
        "user": {
            "username": f"user_{random_string()}",
            "email": f"email_{random_string()}@test.com",
            "password": "pass1234"
        }
    }

    resp = requests.post(f"{base_api_url}/users", json=new_user)
    assert resp.status_code == 200
    data = resp.json()["user"]
    assert "email" in data and "token" in data
