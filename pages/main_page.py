import allure

from elements.locators import MainPageLocators
from elements.main_menu_elements import MainMenu
from elements.subscribe_window_elements import *
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.open('https://www.rbc.ru/')
        self.subscribe_window = SubscribeWindow(self.browser)
        self.main_menu = MainMenu(self.browser)
    @allure.step('Появляется пуш уведомление с предложением подписаться')
    def should_be_subscribe_push_allow(self):
        assert self.subscribe_window.window_is_present(), 'Уведомление не отображается'

    @allure.step('Попытка подписаться')
    def can_subscribe_with_push_allow(self):
        assert 'Вы успешно подписаны на оповещания от RBC.RU' in \
               self.subscribe_window.try_to_subscribe(), 'Подписаться не удалось'

    @allure.step('ЛКМ по отказаться')
    def refuse_subscribe_push_allow(self):
        assert self.subscribe_window.refuse_subscribe(), 'Уведомление не исчезло'

    def open_top_menu_link(self, link_num, link):
        assert self.main_menu.click_menu_button(link_num) == link, 'Переход состоялся'

    # @allure.step('Закрыть окно выбора региона')
    # def apply_geolocation_push_allow(self):
    #     self.close_push_allow(*MainPageLocators.GEOLOCATION_PUSH_ALLOW_YES)
    #
    # @allure.step('Открывается ссылка из меню')
    # def should_open_top_menu_link(self, link_number_and_address):
    #     link_num, address = link_number_and_address
    #     self.click_to_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_num}]')
    #     assert self.browser.current_url == address, 'Страница не соответствует пункту меню'
    #
    # @allure.step('Открывается страница аутентификации')
    # def should_open_auth_link(self):
    #     self.click_to_element(*MainPageLocators.AUTH_TOP_MENU)
    #     self.click_to_element(*MainPageLocators.AUTH_TOP_MENU_ENTER)
    #     assert 'auth.rbc.ru' in self.get_current_url(), 'Не страница аутентификации'
