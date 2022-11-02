from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url='https://www.rbc.ru/', timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def click_to_element(self, method, selector):
        element = self.browser.find_element(method, selector)
        element.click()

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return True
        return False

    def switch_to_last_handle(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])

    def get_text(self, method, selector):
        return self.browser.find_element(method, selector).text

    def close_push_allow(self, method, selector):
        try:
            self.click_to_element(method, selector)
        except NoSuchElementException:
            pass

    def get_current_url(self):
        return self.browser.current_url
