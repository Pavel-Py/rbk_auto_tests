from elements.base_elements import BaseElements


class AuthMenu(BaseElements):
    ENTER_TAB = 'div[data-type="enter"]'
    EMAIL_FIELD = '.js-login-validate input[name="email"]'
    PASS_FIELD = '.js-login-validate input[name = "password"]'
    ENTER_BUTTON = '.js-login-validate .paywall__auth__form__submit'
    PROFILE_EMAIL = '.profile__status__email'
    LOGIN_ERROR_BLOCK = '//div[@style="display: block;"]'

    def select_login_tab(self):
        self.click_to(self.ENTER_TAB)

    def try_to_authorize(self, login: str, password: str):
        self.fill_in_field(self.EMAIL_FIELD, text=login)
        self.fill_in_field(self.PASS_FIELD, text=password)
        self.click_to(self.ENTER_BUTTON)

    def get_login_after_authorise(self):
        return self.get_text(self.PROFILE_EMAIL)

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR_BLOCK, self.XPATH)
