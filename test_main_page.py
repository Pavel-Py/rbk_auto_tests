
import pytest

from pages.main_page import MainPage


class TestSubscribeWindow:
    def test_user_can_subscribe(self, everytime_new_browser):
        page = MainPage(everytime_new_browser)
        page.open()
        page.should_be_subscribe_push_allow()
        page.apply_subscribe_push_allow()
        page.switch_to_last_handle()
        page.check_subscribe_success_text()

    def test_user_can_abandon_subscribe(self, everytime_new_browser):
        page = MainPage(everytime_new_browser)
        page.open()
        page.should_be_subscribe_push_allow()
        page.refuse_subscribe_push_allow()


class TestTopMenu:
    @pytest.mark.parametrize('link_num_and_address', [(1, 'https://tv.rbc.ru/?utm_source=topline'),
                                                      (2, 'https://www.rbc.ru/newspaper/?utm_source=topline'),
                                                      (3, 'https://pro.rbc.ru/'),
                                                      (4, 'https://quote.ru/?utm_source=topline'),
                                                      (5, 'https://spb.plus.rbc.ru/'),
                                                      (6, 'https://www.rbc.ru/neweconomy/?utm_source=topline')
                                                      ])
    def test_user_can_open_top_menu_links(self, session_browser, link_num_and_address):
        page = MainPage(session_browser)
        page.open()
        page.close_subscribe_push_allow()
        page.should_open_top_menu_link(link_num_and_address)

    def test_user_can_open_auth_link(self, session_browser):
        page = MainPage(session_browser)
        page.open()
        page.apply_geolocation_push_allow()
        page.should_open_auth_link()
