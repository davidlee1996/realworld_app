from pages.home_page import HomePage
from pages.navbar import Navbar

def test_navbar_links(page):
    home = HomePage(page)
    nav = Navbar(page)

    home.go_to()
    nav.click_sign_in()
    assert "Sign In" in page.content()

    nav.click_sign_up()
    assert "Sign Up" in page.content()

    nav.click_home()
    assert home.is_global_feed_visible()
