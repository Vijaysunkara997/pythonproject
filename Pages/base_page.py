class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def enter(self, locator, value):
        locator.fill(value)