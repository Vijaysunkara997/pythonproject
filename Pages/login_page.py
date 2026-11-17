from Test.Pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.get_by_role("textbox", name="Username")
        self.button = page.get_by_role("button", name="Primary Action")

    def aur(self):

        self.open("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

        expect(self.button).to_be_visible()
        self.click(self.button)

        expect(self.username).to_be_visible()
        self.enter(self.username, "Vijaykumar")