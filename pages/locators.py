from selenium.webdriver.common.by import By


class MainPageLocators:
    SUBSCRIBE_NO = (By.CSS_SELECTOR, '.push-allow__button[data-type=no]')
    SUBSCRIBE_YES = (By.CSS_SELECTOR, '.push-allow__button[data-type=yes]')
    PUSH_ALLOW_VISIBLE = (By.CSS_SELECTOR, '.push-allow[style="display: block;"]')
    PUSH_ALLOW_HIDDEN = (By.CSS_SELECTOR, '.push-allow[style="display: none;"]')
