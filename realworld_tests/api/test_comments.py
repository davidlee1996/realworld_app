import pytest
pytestmark = pytest.mark.api

def test_post_comment(base_api_url, auth_token):
    headers = {"Authorization": f"Token {auth_token}"}
    # Create article
    article_data = {
        "article": {
            "title": f"Article with comment {random_string()}",
            "description": "desc",
            "body": "body",
            "tagList": []
        }
    }
    article_resp = requests.post(f"{base_api_url}/articles", headers=headers, json=article_data)
    slug = article_resp.json()["article"]["slug"]

    # Post comment
    comment_data = {"comment": {"body": "Nice post!"}}
    comment_resp = requests.post(f"{base_api_url}/articles/{slug}/comments", headers=headers, json=comment_data)
    assert comment_resp.status_code == 200
    assert comment_resp.json()["comment"]["body"] == "Nice post!"
