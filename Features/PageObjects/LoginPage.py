import os

from Features.PageObjects.BasePage import BasePage
from Utilities import Controller as con


class LoginPage(BasePage):
    # Section name from config.ini file
    section = "LOGIN_PAGE"

    def __init__(self,page):
        super().__init__(page)

    def signup_enter_name(self, signup_name=None):
        if signup_name is None:
            signup_name = con.get_random_text(8)
        self.type_in(self.section, "signup_name_input_field_css", signup_name)
        return signup_name

    def signup_enter_signup_email(self,signup_email=None):
        if signup_email is None:
            signup_email = f"{con.get_cur_dt()}_{con.get_cur_time()}@yopmail.com"
        self.type_in(self.section, "signup_email_input_field_css", signup_email)
        return signup_email

    def click_signup_submit_btn(self):
        self.do_click(self.section, "signup_submit_signup_btn_css")

    def enter_username(self, username=None):
        if username is None:
            username = os.environ.get("USER_EMAIL")
        self.type_in(self.section, "login_email_input_field_css", username)

    def enter_password(self,password=None):
        if password is None:
            password = os.environ.get("PASSWORD")
        self.type_in(self.section, "login_password_input_field_css", password)

    def submit_login(self):
        self.do_click(self.section, "login_submit_signup_btn_css")