import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def everytime_new_browser():
    options = Options()
    options.page_load_strategy = 'eager'
    # options.add_argument('--headless')
    options.add_argument('--window-size=1600,800')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    options.add_argument("--enable-notifications")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def session_browser():
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument('--headless')
    options.add_argument('--window-size=1600,800')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    options.add_argument("--enable-notifications")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
