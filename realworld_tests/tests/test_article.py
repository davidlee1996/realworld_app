from pages.login_page import LoginPage
from pages.editor_page import EditorPage
from pages.navbar import Navbar

def test_create_article(page):
    login = LoginPage(page)
    editor = EditorPage(page)
    nav = Navbar(page)

    login.go_to()
    login.fill_email("testuser@example.com")
    login.fill_password("testpassword")
    login.submit()

    page.click('a.nav-link:has-text("New Article")')
    editor.fill_article("Test Article", "Test About", "This is a test body.", "pytest")
    editor.submit_article()

    assert editor.is_article_published()
