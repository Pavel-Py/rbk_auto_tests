import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument("--window-size=1600,800")
    browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
    yield browser
    browser.quit()
