from elements.auth_menu import AuthMenu
from .base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.open('https://auth.rbc.ru/login')
        self.auth_menu = AuthMenu(self.browser)

    def user_should_authorise(self, login, password):
        self.auth_menu.select_login_tab()
        self.auth_menu.try_to_authorize(login, password)
        assert self.auth_menu.get_login_after_authorise() == login, 'Авторизация не удалась'

    def should_be_incorrect_password_error(self, login, password):
        error_text = 'Пользователя с таким e-mail не существует или введен неверный пароль'
        self.auth_menu.select_login_tab()
        self.auth_menu.try_to_authorize(login, password)
        assert error_text == self.auth_menu.get_login_error(), 'Сообщение не соответствует ошибке'

    def should_be_empty_field_error(self, login, password):
        error_text = 'Не все поля заполнены'
        self.auth_menu.select_login_tab()
        self.auth_menu.try_to_authorize(login, password)
        assert error_text == self.auth_menu.get_login_error(), 'Сообщение не соответствует ошибке'
