from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseElements:
    def __init__(self, browser):
        self.browser = browser
    CSS_SELECTOR = By.CSS_SELECTOR
    XPATH = By.XPATH

    def is_present(self, selector: str, method=CSS_SELECTOR) -> bool:
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def click_to(self, selector: str, method=CSS_SELECTOR):
        self.browser.find_element(method, selector).click()

    def get_text(self, selector: str, method=CSS_SELECTOR) -> str:
        return self.browser.find_element(method, selector).text

    def is_not_element_present(self, selector: str, method=CSS_SELECTOR):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return True
        return False

    def fill_in_field(self, selector: str, method=CSS_SELECTOR, text: str = ''):
        self.browser.find_element(method, selector).send_keys(text)

    def switch_to_last_handle(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])

    def current_url(self):
        return self.browser.current_url

