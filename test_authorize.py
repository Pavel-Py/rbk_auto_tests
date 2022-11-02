import time

import pytest

from pages.auth_page import AuthPage


def test_user_can_auth_with_valid_data(session_browser):
    page = AuthPage(session_browser)
    page.open()
    page.select_login_tab()
    page.user_should_authorise('testmail2024@mail.ru', '[htymrfrfznj')


@pytest.mark.parametrize('data', [('testmail2024@mail.ru', 'wrong_pass'),
                                  ('wrong@email.com', 'wrong_pass')
                                  ])
def test_user_cant_auth_with_invalid_data(session_browser, data):
    page = AuthPage(session_browser)
    page.open()
    page.select_login_tab()
    page.should_be_incorrect_password_error(data)
