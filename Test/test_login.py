from Pages.login_page import LoginPage


class TestLogin:

    def test_login(self, page):

        bg = LoginPage(page)
        bg.aur()