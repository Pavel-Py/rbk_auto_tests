import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_be_subscribe_push_allow(self):
        assert self.is_element_present(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_VISIBLE)

    def apply_subscribe_push_allow(self):
        self.click_to_element(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_YES)

    def refuse_subscribe_push_allow(self):
        self.click_to_element(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_NO)
        assert self.is_element_present(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_HIDDEN)

    def check_subscribe_success_text(self):
        text = self.get_text(*MainPageLocators.SUCCESS_SUBSCRIBE_TEXT)
        assert 'Вы успешно подписаны' in text

    def close_subscribe_push_allow(self):
        self.close_push_allow(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_NO)

    def apply_geolocation_push_allow(self):
        self.close_push_allow(*MainPageLocators.GEOLOCATION_PUSH_ALLOW_YES)

    def should_open_top_menu_link(self, link_number_and_address):
        link_num, address = link_number_and_address
        self.click_to_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_num}]')
        assert self.browser.current_url == address

    def should_open_auth_link(self):
        self.click_to_element(*MainPageLocators.AUTH_TOP_MENU)
        self.click_to_element(*MainPageLocators.AUTH_TOP_MENU_ENTER)
        assert 'auth.rbc.ru' in self.get_current_url()
