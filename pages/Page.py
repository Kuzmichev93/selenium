import time

from selenium.webdriver.common.by import By

from pages.Base import Base


class Page(Base):
    def __init__(self,browser):
        super().__init__(browser)

    def check_search(self):
        result = self.browser.find_element(By.TAG_NAME,"input")
        return result.is_displayed()

    def get_value_input(self):
        result = self.browser.find_element(By.TAG_NAME,"input")
        result.send_keys("ozon")
        time.sleep(5)
        return result.get_attribute("value")

    def get_windows_suggest(self):
        result = self.browser.find_element(By.CLASS_NAME,"mini-suggest__popup-content")
        time.sleep(5)
        return result.is_displayed()

    def get_len_windows_suggest(self):
        result = self.browser.find_element(By.CLASS_NAME,"mini-suggest__group")
        time.sleep(5)
        array = result.find_elements(By.XPATH, '*')
        return array


    def check_suggest(self):
        result = self.browser.find_element(By.TAG_NAME,"input")
        result.send_keys("ozon")
        time.sleep(10)

