import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def browser():
    s = Service(os.path.join(os.path.curdir, 'chromedriver'))
    options = Options()
    options.add_argument("--window-size=1600,800")
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    browser.quit()
