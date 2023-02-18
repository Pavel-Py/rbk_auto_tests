import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, browser, timeout=2):
        self.browser = browser
        self.url = 'https://www.rbc.ru/'
        self.browser.implicitly_wait(timeout)


    def is_not_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return True
        return False

    @allure.step('Переход в открывшуюся вкладку')
    def switch_to_last_handle(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])


    def close_push_allow(self, method, selector):
        try:
            self.click_to_element(method, selector)
        except NoSuchElementException:
            pass

    def get_current_url(self):
        return self.browser.current_url

    def fill_in_field(self, method, selector, data):
        self.browser.find_element(method, selector).send_keys(data)

    def wait_url_change(self):
        WebDriverWait(self.browser, 5).until(ec.url_changes(self.url))
