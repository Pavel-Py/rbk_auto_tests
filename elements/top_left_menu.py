from elements.base_elements import BaseElements


class TopLeftMenu(BaseElements):
    BASE_BUTTON = f'//div[@class="topline__projects"]/'
    TV = BASE_BUTTON + 'div[1]'
    PRO = BASE_BUTTON + 'div[2]'
    INVEST = BASE_BUTTON + 'div[3]'
    EVENTS = BASE_BUTTON + 'div[4]'
    PLUS = BASE_BUTTON + 'div[5]'
    BUTTONS = {1: TV, 2: PRO, 3: INVEST, 4: EVENTS, 5: PLUS}

    def click_menu_button(self, link_num: int):
        self.click_to(self.BUTTONS[link_num], method=self.XPATH)
        return self.current_url()

    def go_main_page(self):
        self.browser.get('https://www.rbc.ru/')
