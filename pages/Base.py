class Base:
    def __init__(self,browser):
        self.browser = browser

    def get_page(self):
        self.browser.get("https://ya.ru/")