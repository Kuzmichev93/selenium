import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    chrome_br = webdriver.Chrome()
    chrome_br.implicitly_wait(15)
    chrome_br.get("https://ya.ru/")
    return chrome_br

@pytest.fixture()
def suggest_windows():
    chrome_br = webdriver.Chrome()
    chrome_br.implicitly_wait(15)
    chrome_br.get("https://ya.ru/")
    chrome_br.find_element(By.TAG_NAME,"input").send_keys("ozon")
    return chrome_br