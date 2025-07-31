import pytest
pytestmark = pytest.mark.api

def test_create_article(base_api_url, auth_token):
    headers = {"Authorization": f"Token {auth_token}"}
    article_data = {
        "article": {
            "title": f"My Article {random_string()}",
            "description": "Description",
            "body": "This is a test article",
            "tagList": ["test", "api"]
        }
    }
    resp = requests.post(f"{base_api_url}/articles", headers=headers, json=article_data)
    assert resp.status_code == 200
    assert "slug" in resp.json()["article"]

def test_get_article_by_slug(base_api_url, auth_token):
    headers = {"Authorization": f"Token {auth_token}"}
    # Create article
    article_data = {
        "article": {
            "title": f"My Article {random_string()}",
            "description": "Desc",
            "body": "Body",
            "tagList": []
        }
    }
    post_resp = requests.post(f"{base_api_url}/articles", headers=headers, json=article_data)
    slug = post_resp.json()["article"]["slug"]

    # Fetch it
    get_resp = requests.get(f"{base_api_url}/articles/{slug}", headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["article"]["slug"] == slug
