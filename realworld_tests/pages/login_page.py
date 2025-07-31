from pages.base_page import BasePage

class LoginPage(BasePage):
    def go_to(self):
        self.page.goto("https://demo.realworld.io/#/login")

    def fill_email(self, email):
        self.page.fill('input[type="email"]', email)

    def fill_password(self, password):
        self.page.fill('input[type="password"]', password)

    def submit(self):
        self.page.click('button[type="submit"]')

    def error_message_visible(self):
        self.page.wait_for_timeout(1000)
        return self.page.locator("text=email or password is invalid").is_visible()
