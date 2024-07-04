import time

from selenium.webdriver.common.by import By

from conftest import browser,suggest_windows
from pages.Image import Image


def test_get_href_iamge(browser):
    browser = Image(browser)
    browser.get_page()
    get_array = browser.get_href_iamge()
    Array = []
    for k in get_array:
        Array.append(k.find_element(By.TAG_NAME,"a").get_attribute("aria-label"))
    if "Картинки" not in Array:
        raise AssertionError("Элемента Картинки нет в списке")

def test_get_page_image(browser):
    browser = Image(browser)
    browser.get_page()
    assert browser.get_page_image() == "https://ya.ru/images/"

def test_get_href_image(browser):
    browser = Image(browser)
    browser.get_page()
    assert browser.get_href()[0] == browser.get_href()[1]