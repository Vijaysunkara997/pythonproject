from Pages.login_page import LoginPage


class TestLogin:

    def test_login(self, page):
        login = LoginPage(page)
        login.login_flipkart()