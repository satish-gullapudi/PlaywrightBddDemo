from Features.PageObjects.BasePage import BasePage
import Utilities.Locators as loc


class HeaderNav(BasePage):
    section = "HEADER_NAV_LINKS"

    def __init__(self,page):
        super().__init__(page)

    def click_header_login_naav_link(self):
        self.do_click(self.section, "header_login_nav_link_css")

    def click_header_contact_us_nav_link(self):
        self.do_click(self.section, "header_contactus_nav_link_css")

    def click_logout(self):
        self.do_click(self.section, "header_logout_nav_link_css")