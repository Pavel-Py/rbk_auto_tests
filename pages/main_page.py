from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import TopMenuLocators, MainPageLocators


class TopMenu(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def close_push_subscribe(self):
        self.browser.find_element(*MainPageLocators.SUBSCRIBE_NO).click()

    def click_on_link(self, link_number):
        link = self.browser.find_element(By.XPATH, f'//div[@class="topline__projects"]/div[{link_number}]')
        link.click()



