from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = "[name='q']"
        self.search_button = "[name='btnK']"

    def navigate(self):
        self.page.goto("https://www.google.com")

    def search(self, query: str):
        self.page.fill(self.search_box, query)
        self.page.press(self.search_box, "Enter")