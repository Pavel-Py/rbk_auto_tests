from elements.base_elements import BaseElements


class SubscribeWindow(BaseElements):
    window = '.push-allow[style="display: block;"]'
    yes_button = '.push-allow__button[data-type=yes]'
    no_button = '.push-allow__button[data-type=no]'
    result_text = '.subscribe__text[style="display: block;"]'
    hidden_window = '.push-allow[style="display: none;"]'

    def window_is_exist(self):
        return self.element_exist(self.method, self.window)

    def click_yes_button(self):
        self.click_to_element(self.method, self.yes_button)

    def click_no_button(self):
        self.click_to_element(self.method, self.no_button)

    def get_result_text(self):
        return self.get_text(self.method, self.result_text)

    def window_is_hidden(self):
        return self.element_exist(self.method, self.hidden_window)
