from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class TopMenu(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def close_push_subscribe(self):
        try:
            refuse_subscribe = self.browser.find_element(*MainPageLocators.SUBSCRIBE_NO)
            refuse_subscribe.click()
        except NoSuchElementException:
            pass

    def click_on_link(self, link_number_and_address):
        link_num, address = link_number_and_address
        link = self.browser.find_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_num}]')
        link.click()
        print(self.browser.current_url, address)
        assert self.browser.current_url == address
