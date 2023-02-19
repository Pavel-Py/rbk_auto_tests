from selenium.webdriver.common.by import By


class MainPageLocators:
    SUBSCRIBE_PUSH_ALLOW_NO = (By.CSS_SELECTOR, '.push-allow__button[data-type=no]')
    SUBSCRIBE_PUSH_ALLOW_YES = (By.CSS_SELECTOR, '.push-allow__button[data-type=yes]')
    SUBSCRIBE_PUSH_ALLOW_VISIBLE = (By.CSS_SELECTOR, '.push-allow[style="display: block;"]')
    SUBSCRIBE_PUSH_ALLOW_HIDDEN = (By.CSS_SELECTOR, '.push-allow[style="display: none;"]')
    GEOLOCATION_PUSH_ALLOW_YES = (By.CSS_SELECTOR, '.topline__region__detector__button')
    SUCCESS_SUBSCRIBE_TEXT = (By.CSS_SELECTOR, '.subscribe__text[style="display: block;"]')
    AUTH_TOP_MENU = (By.CSS_SELECTOR, '.topline__auth__link')
    AUTH_TOP_MENU_ENTER = (By.XPATH, '//div[@class="topline__auth__profile__menu"]/div[1]/a')


class AuthPageLocators:
    LOGIN_TAB = (By.CSS_SELECTOR, 'div[data-type="enter"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '.js-login-validate input[name="email"]')
    PASS_FIELD = (By.CSS_SELECTOR, '.js-login-validate input[name = "password"]')
    ENTER_BUTTON = (By.CSS_SELECTOR, '.js-login-validate .paywall__auth__form__submit')
    LOGIN_ERROR_BLOCK = (By.XPATH, '//div[@style="display: block;"]')
