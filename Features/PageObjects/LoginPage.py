from Features.PageObjects.BasePage import BasePage
import Utilities.Locators as loc


class LoginPage(BasePage):
    section = "login_page"

    def __init__(self,page):
        super().__init__(page)

    def enter_username(self, username):
        self.type(loc.get_login_page_username_field_locator(), username)

    def enter_password(self,password):
        self.type(loc.get_login_page_password_field_locator(),password)

    def submit_login(self):
        self.do_click(loc.get_login_page_submit_login_btn_locator())