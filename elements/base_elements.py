from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseElements:
    def __init__(self, browser):
        self.browser = browser
    method = By.CSS_SELECTOR
    selector = ''

    def element_exist(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def click_to_element(self, method, selector):
        self.browser.find_element(method, selector).click()

    def get_text(self, method, selector):
        return self.browser.find_element(method, selector).text


