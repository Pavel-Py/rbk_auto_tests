from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseElements:
    def __init__(self, browser):
        self.browser = browser
    css_selector = By.CSS_SELECTOR
    xpath = By.XPATH

    def is_present(self, selector: str, method=css_selector) -> bool:
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def click_to(self, selector: str, method=css_selector):
        self.browser.find_element(method, selector).click()

    def get_text(self, selector: str, method=css_selector) -> str:
        return self.browser.find_element(method, selector).text

    def is_not_element_present(self, selector: str, method=css_selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return True
        return False

    def switch_to_last_handle(self):
        handles = self.browser.window_handles
        self.browser.switch_to.WINDOW(handles[-1])

    def current_url(self):
        return self.browser.current_url()
