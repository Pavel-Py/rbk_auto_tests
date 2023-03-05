import time

from selenium.common import NoSuchElementException

from elements.base_elements import BaseElements


class SubscribeWindow(BaseElements):
    WINDOW = '.push-allow[style="display: block;"]'
    YES_BUTTON = '.push-allow__button[data-type=yes]'
    NO_BUTTON = '.push-allow__button[data-type=no]'
    RESULT_TEXT = '.subscribe__text[style="display: block;"]'
    HIDDEN_WINDOW = '.push-allow[style="display: none;"]'

    def window_is_present(self):
        return self.is_present(self.WINDOW)

    def try_to_subscribe(self):
        self.click_to(self.YES_BUTTON)
        self.switch_to_last_handle()
        return self.get_text(self.RESULT_TEXT)

    def refuse_subscribe(self):
        self.click_to(self.NO_BUTTON)
        return self.is_present(self.HIDDEN_WINDOW)

    def close_subscribe_push_allow(self):
        try:
            self.click_to(self.NO_BUTTON)
        except NoSuchElementException:
            pass
