import time

from selenium.webdriver.common.by import By

from pages.Base import Base


class Image(Base):
    def __init__(self,browser):
        super().__init__(browser)

    def get_href_iamge(self):
        self.browser.find_element(By.TAG_NAME,"input").click()
        time.sleep(5)
        result  = self.browser.find_elements(By.CLASS_NAME,"services-suggest__list-item")

        return result

    def get_page_image(self):
        self.browser.find_element(By.TAG_NAME,"input").click()
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,"services-suggest__list-item-more").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div[18]/div/div/div/div[1]/div/div/div[2]/ul/li[9]").click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self.browser.current_url

    def get_href(self):
        self.browser.find_element(By.TAG_NAME,"input").click()
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,"services-suggest__list-item-more").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div[18]/div/div/div/div[1]/div/div/div[2]/ul/li[9]").click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.find_elements(By.CLASS_NAME,"PopularRequestList").click()
        time.sleep(3)
        data = self.browser.find_elements(By.CLASS_NAME,"JustifierRowLayout-Row")
        data[0].click()
        image = self.browser.find_element(By.CLASS_NAME,"ImagesViewer-LayoutScene")
        result = image.find_elements(By.XPATH,'*')
        result[5].click()
        href = self.browser.current_url
        time.sleep(3)
        result[4].click()
        return [self.browser.current_url,href]


