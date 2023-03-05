import allure

from elements.top_left_menu import TopLeftMenu
from elements.subscribe_window import SubscribeWindow
from elements.top_right_menu import TopRightMenu
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.open('https://www.rbc.ru/')
        self.subscribe_window = SubscribeWindow(self.browser)
        self.top_left_menu = TopLeftMenu(self.browser)
        self.top_right_menu = TopRightMenu(self.browser)

    @allure.step('Появляется пуш уведомление с предложением подписаться')
    def should_be_subscribe_push_allow(self):
        assert self.subscribe_window.window_is_present(), 'Уведомление не отображается'

    @allure.step('Попытка подписаться')
    def can_subscribe_with_push_allow(self):
        assert 'Вы успешно подписаны на оповещания от RBC.RU' in \
               self.subscribe_window.try_to_subscribe(), 'Подписаться не удалось'

    @allure.step('ЛКМ по отказаться')
    def can_refuse_subscribe_push_allow(self):
        assert self.subscribe_window.refuse_subscribe(), 'Уведомление не исчезло'

    @allure.step('Открывается ссылка из меню')
    def should_open_top_menu_link(self, link_num: int, link: str):
        assert self.top_left_menu.click_menu_button(link_num) == link, 'Страница не соответствует пункту меню'

    @allure.step('Открывается страница аутентификации')
    def should_open_auth_link(self):
        self.top_right_menu.apply_geolocation_push_allow()
        assert 'auth.rbc.ru' in self.top_right_menu.go_auth_page(), 'Не страница аутентификации'
