import allure

from .locators import MainPageLocators
from .base_page import BasePage
from .page_elements import *


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.browser.get(self.url)
        self.subscribe_push_window = SubscribeWindow(self.browser)

    @allure.step('Появляется пуш уведомление с предложением подписаться')
    def should_be_subscribe_push_allow(self):
        assert self.subscribe_push_window.element_exist(), 'Уведомление не отображается'

    @allure.step('Попытка подписаться')
    def user_can_subscribe(self):
        self.subscribe_push_window.click_yes_button()
        self.switch_to_last_handle()
        assert 'Вы успешно подписаны на оповещания от RBC.RU' in self.subscribe_push_window.get_subscribe_text()


    @allure.step('ЛКМ по отказаться')
    def refuse_subscribe_push_allow(self):
        self.click_to_element(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_NO)
        assert self.is_element_present(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_HIDDEN), 'Уведомление не исчезло'

    @allure.step('Проверка успешности')
    def check_subscribe_success_text(self):
        text = self.get_text(*MainPageLocators.SUCCESS_SUBSCRIBE_TEXT)
        assert 'Вы успешно подписаны' in text, 'Нет текста "Вы успешно подписаны"'

    @allure.step('Закрыть окно подписки')
    def close_subscribe_push_allow(self):
        self.close_push_allow(*MainPageLocators.SUBSCRIBE_PUSH_ALLOW_NO)

    @allure.step('Закрыть окно выбора региона')
    def apply_geolocation_push_allow(self):
        self.close_push_allow(*MainPageLocators.GEOLOCATION_PUSH_ALLOW_YES)

    @allure.step('Открывается ссылка из меню')
    def should_open_top_menu_link(self, link_number_and_address):
        link_num, address = link_number_and_address
        self.click_to_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_num}]')
        assert self.browser.current_url == address, 'Страница не соответствует пункту меню'

    @allure.step('Открывается страница аутентификации')
    def should_open_auth_link(self):
        self.click_to_element(*MainPageLocators.AUTH_TOP_MENU)
        self.click_to_element(*MainPageLocators.AUTH_TOP_MENU_ENTER)
        assert 'auth.rbc.ru' in self.get_current_url(), 'Не страница аутентификации'
