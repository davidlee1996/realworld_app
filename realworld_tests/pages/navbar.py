from pages.base_page import BasePage

class Navbar(BasePage):
    def click_home(self):
        self.page.click('a.nav-link:has-text("Home")')

    def click_sign_in(self):
        self.page.click('a.nav-link:has-text("Sign in")')

    def click_sign_up(self):
        self.page.click('a.nav-link:has-text("Sign up")')

    def is_logged_in(self, username):
        return self.page.locator(f'a.nav-link:has-text("{username}")').is_visible()
