import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_be_subscribe_push_allow(self):
        assert self.is_element_present(*MainPageLocators.PUSH_ALLOW_VISIBLE)

    def apply_subscribe_push_allow(self):
        apply_button = self.browser.find_element(*MainPageLocators.SUBSCRIBE_YES)
        apply_button.click()
        """ НАДО КАК ТО РАЗРЕШИТЬ УВЕДОМЛЕНИЯ"""

    def refuse_subscribe_push_allow(self):
        apply_button = self.browser.find_element(*MainPageLocators.SUBSCRIBE_NO)
        apply_button.click()
        assert self.is_element_present(*MainPageLocators.PUSH_ALLOW_HIDDEN)

    def close_subscribe_push_allow(self):
        try:
            refuse_button = self.browser.find_element(*MainPageLocators.SUBSCRIBE_NO)
            refuse_button.click()
        except NoSuchElementException:
            pass

    def should_open_link(self, link_number_and_address):
        link_num, address = link_number_and_address
        link = self.browser.find_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_num}]')
        link.click()
        assert self.browser.current_url == address
