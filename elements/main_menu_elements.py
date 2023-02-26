from elements.base_elements import BaseElements


class MainMenu(BaseElements):
    base_button = f'//div[@class="topline__projects"]/'
    tv = base_button + 'div[1]'
    pro = f'//div[@class="topline__projects"]/div[2]'
    invest = f'//div[@class="topline__projects"]/div[3]'
    events = f'//div[@class="topline__projects"]/div[4]'
    plus = f'//div[@class="topline__projects"]/div[5]'

    # def click_menu_button(self):
    #     self.tv.