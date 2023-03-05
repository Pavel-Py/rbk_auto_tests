from elements.base_elements import BaseElements


class TopRightMenu(BaseElements):
    AUTH = '.topline__auth__link'
    ENTER = '//div[@class="topline__auth__profile__menu"]/div[1]/a'
    REGION_DETECTOR_YES = '.topline__region__detector__button'

    def apply_geolocation_push_allow(self):
        self.click_to(self.REGION_DETECTOR_YES)

    def go_auth_page(self):
        self.click_to(self.AUTH)
        self.click_to(self.ENTER, self.XPATH)
        return self.current_url()
