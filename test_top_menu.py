import pytest
from pages.main_page import TopMenu


def test_user_can_open_menu_link(browser):
    url = 'https://www.rbc.ru/'
    page = TopMenu(browser, url)
    page.open()
    page.close_push_subscribe()
    page.click_on_link(2)

