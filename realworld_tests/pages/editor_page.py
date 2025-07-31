from pages.base_page import BasePage

class EditorPage(BasePage):
    def go_to(self):
        self.page.goto("https://demo.realworld.io/#/editor")

    def fill_article(self, title, about, body, tags):
        self.page.fill('input[placeholder="Article Title"]', title)
        self.page.fill('input[placeholder*="this article about?"]', about)
        self.page.fill('textarea[placeholder*="Write your article"]', body)
        self.page.fill('input[placeholder="Enter tags"]', tags)

    def submit_article(self):
        self.page.click('button[type="button"]')

    def is_article_published(self):
        return self.page.locator("h1").is_visible()
