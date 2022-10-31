import pytest
from pages.main_page import MainPage


class TestSubscribeWindow:

    def test_user_can_abandon_subscribe(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_subscribe_push_allow()
        page.refuse_subscribe_push_allow()

    def test_user_can_subscribe(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_subscribe_push_allow()
        page.apply_subscribe_push_allow()


class TestTopMenu:
    @pytest.mark.parametrize('link_num_and_address', [(1, 'https://tv.rbc.ru/?utm_source=topline'),
                                                      (2, 'https://www.rbc.ru/newspaper/?utm_source=topline'),
                                                      (3, 'https://pro.rbc.ru/'),
                                                      (4, 'https://quote.ru/?utm_source=topline'),
                                                      (5, 'https://spb.plus.rbc.ru/'),
                                                      (6, 'https://www.rbc.ru/neweconomy/?utm_source=topline')
                                                      ])
    def test_user_can_open_top_menu_links(self, browser, link_num_and_address):
        page = MainPage(browser)
        page.open()
        page.close_subscribe_push_allow()
        page.should_open_link(link_num_and_address)


