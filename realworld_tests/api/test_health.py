import pytest
pytestmark = pytest.mark.api

def test_articles_feed_available(base_api_url):
    response = requests.get(f"{base_api_url}/articles")
    assert response.status_code == 200
    assert "articles" in response.json()
