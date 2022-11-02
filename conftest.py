import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def everytime_new_browser():
    s = Service(os.path.join(os.path.curdir, 'chromedriver'))
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1600,800")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def session_browser():
    s = Service(os.path.join(os.path.curdir, 'chromedriver'))
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1600,800")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    browser.quit()
