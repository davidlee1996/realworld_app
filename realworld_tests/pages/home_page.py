from pages.base_page import BasePage

class HomePage(BasePage):
    def go_to(self):
        self.page.goto("https://demo.realworld.io/#/")

    def get_title(self):
        return self.page.title()

    def is_sign_in_visible(self):
        return self.page.locator("text=Sign in").is_visible()

    def is_global_feed_visible(self):
        return self.page.locator("text=Global Feed").is_visible()
