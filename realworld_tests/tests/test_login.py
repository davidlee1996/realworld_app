from pages.login_page import LoginPage
from pages.navbar import Navbar

def test_login_success(page):
    login = LoginPage(page)
    nav = Navbar(page)

    login.go_to()
    login.fill_email("testuser@example.com")   # Make sure this user exists
    login.fill_password("testpassword")
    login.submit()

    assert nav.is_logged_in("testuser")
