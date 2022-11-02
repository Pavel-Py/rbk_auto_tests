from pages.auth_page import AuthPage


def test_user_can_auth_with_valid_data(everytime_new_browser):
    url = ''
    page = AuthPage(everytime_new_browser)
