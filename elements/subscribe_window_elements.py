from elements.base_elements import BaseElements
from pages.base_page import BasePage


class SubscribeWindow(BaseElements):
    window = '.push-allow[style="display: block;"]'
    yes_button = '.push-allow__button[data-type=yes]'
    no_button = '.push-allow__button[data-type=no]'
    result_text = '.subscribe__text[style="display: block;"]'
    hidden_window = '.push-allow[style="display: none;"]'

    def should_be_subscribe_push_allow(self):
        return self.is_present(self.window)

    def user_can_subscribe(self):
        self.click_to(self.yes_button)
        self.switch_to_last_handle()
        return self.get_text(self.result_text)
