import pytest
pytestmark = pytest.mark.api

def test_get_tags(base_api_url):
    resp = requests.get(f"{base_api_url}/tags")
    assert resp.status_code == 200
    assert "tags" in resp.json()
    assert isinstance(resp.json()["tags"], list)
