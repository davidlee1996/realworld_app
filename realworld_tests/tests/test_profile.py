from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.navbar import Navbar

def test_view_profile(page):
    login = LoginPage(page)
    profile = ProfilePage(page)
    nav = Navbar(page)

    login.go_to()
    login.fill_email("testuser@example.com")
    login.fill_password("testpassword")
    login.submit()

    username = "testuser"
    profile.go_to_profile(username)
    assert page.locator("h4").text_content() == username
