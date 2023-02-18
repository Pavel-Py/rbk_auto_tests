from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseElements:
    def __init__(self, browser):
        self.locator = ('method', 'selector')
        self.browser = browser

    def element_exist(self):
        try:
            self.browser.find_element(*self.locator)
        except NoSuchElementException:
            return False
        return True

    def click_to_element(self, locator):
        self.browser.find_element(*locator).click()

    def get_text(self, locator):
        return self.browser.find_element(*locator).text


class SubscribeWindow(BaseElements):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locator = (By.CSS_SELECTOR, '.push-allow[style="display: block;"]')
        self.yes_button = (By.CSS_SELECTOR, '.push-allow__button[data-type=yes]')
        self.subscribe_text = (By.CSS_SELECTOR, '.subscribe__text[style="display: block;"]')

    def click_yes_button(self):
        self.click_to_element(self.yes_button)

    def get_subscribe_text(self):
        return self.get_text(self.subscribe_text)

