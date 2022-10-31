import pytest
from pages.main_page import TopMenu


@pytest.mark.parametrize('link_num_and_address', [(1, 'https://tv.rbc.ru/?utm_source=topline'),
                                                  (2, 'https://www.rbc.ru/newspaper/?utm_source=topline'),
                                                  (3, 'https://pro.rbc.ru/'),
                                                  (4, 'https://quote.ru/?utm_source=topline'),
                                                  (5, 'https://spb.plus.rbc.ru/'),
                                                  (6, 'https://www.rbc.ru/neweconomy/?utm_source=topline'),
                                                  (7, 'https://trends.rbc.ru/trends/?utm_source=topline'),
                                                  (8, 'https://realty.rbc.ru/?utm_source=topline'),
                                                  (9, 'https://sportrbc.ru/?utm_source=topline'),
                                                  (10, 'https://style.rbc.ru/?utm_source=topline')
                                                  ])
def test_user_can_open_menu_link(browser, link_num_and_address):
    url = 'https://www.rbc.ru/'
    page = TopMenu(browser, url)
    page.open()
    page.close_push_subscribe()
    page.click_on_link(link_num_and_address)
