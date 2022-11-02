import time

from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = 'https://auth.rbc.ru/login'

    def select_login_tab(self):
        self.click_to_element(*AuthPageLocators.LOGIN_TAB)

    def user_try_authorise(self, login, password):
        self.fill_in_field(*AuthPageLocators.EMAIL_FIELD, login)
        self.fill_in_field(*AuthPageLocators.PASS_FIELD, password)
        self.click_to_element(*AuthPageLocators.ENTER_BUTTON)

    def user_should_authorise(self, login, password):
        url_after_auth = "https://auth.rbc.ru/profile/payment"
        self.user_try_authorise(login, password)
        self.wait_url_change()
        assert self.get_current_url() == url_after_auth

    def should_be_incorrect_password_error(self, data):
        error_text = 'Пользователя с таким e-mail не существует или введен неверный пароль'
        login, password = data
        self.user_try_authorise(login, password)
        assert error_text == self.get_text(*AuthPageLocators.LOGIN_ERROR_BLOCK)
