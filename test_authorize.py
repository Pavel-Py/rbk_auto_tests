import pytest
import allure
from pages.auth_page import AuthPage


@allure.suite('Авторизация')
class TestAuthorise:
    @allure.feature('Авторизация с валидными данными')
    def test_user_can_auth_with_valid_data(self, everytime_new_browser):
        page = AuthPage(everytime_new_browser)
        page.open()
        page.select_login_tab()
        page.user_should_authorise('testmail2024@mail.ru', '[htymrfrfznj')

    @allure.feature('Авторизация с не валидными данными')
    @pytest.mark.parametrize('data', [('testmail2024@mail.ru', 'wrong_pass'),
                                      ('wrong@email.com', 'wrong_pass')
                                      ])
    def test_user_cant_auth_with_invalid_data(self, session_browser, data):
        page = AuthPage(session_browser)
        page.open()
        page.select_login_tab()
        page.should_be_incorrect_password_error(data)

    @allure.feature('Авторизация с не заполненными полями')
    @pytest.mark.parametrize('data', [('testmail2024@mail.ru', ''),
                                      ('', 'password')
                                      ])
    def test_user_cant_auth_with_empty_fields(self, session_browser, data):
        page = AuthPage(session_browser)
        page.open()
        page.select_login_tab()
        page.should_be_empty_field_error(data)
