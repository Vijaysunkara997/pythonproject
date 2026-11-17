
from Pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.login = page.get_by_role("link", name="Login").first
        self.mobile = page.get_by_role("spinbutton", name="Phone Number")
        self.otp = page.get_by_role("button", name="Continue")

    def login_flipkart(self):
        self.open("https://www.flipkart.com/")

        self.click(self.login)

        expect(self.mobile).to_be_visible()

        self.enter(self.mobile, "8121362508")

        expect(self.otp).to_be_enabled()

        self.click(self.otp)