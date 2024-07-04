import time

from conftest import browser,suggest_windows
from pages.Base import Base
from pages.Page import Page


def test_pd(browser):
    browser = Page(browser)
    browser.get_page()
    result = browser.check_search()
    assert result == True

def test_get_value_input(browser):


    browser = Page(browser)
    browser.get_page()
    assert browser.get_value_input() == "ozon"

def test_get_windows_suggest(suggest_windows):
    browser = Page(suggest_windows)
    assert browser.get_windows_suggest() == True

def test_get_len_windows_suggest(suggest_windows):


    browser = Page(suggest_windows)
    len_array = browser.get_len_windows_suggest()
    assert len(len_array) == 5

def test_get_href_windows_suggest(suggest_windows):


    browser = Page(suggest_windows)
    respons_array = browser.get_len_windows_suggest()
    Array = []
    for k in respons_array:
        Array.append(k.get_attribute("href"))
    if "https://www.ozon.ru/" not in Array:
        raise AssertionError("В 5 элементах нет ссылки https://www.ozon.ru/")



