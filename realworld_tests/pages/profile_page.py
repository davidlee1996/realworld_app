from pages.base_page import BasePage

class ProfilePage(BasePage):
    def go_to_profile(self, username):
        self.page.goto(f"https://demo.realworld.io/#/@{username}")

    def is_article_listed(self, title):
        return self.page.locator(f"h1:has-text('{title}')").is_visible()
