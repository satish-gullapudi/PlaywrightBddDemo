import os
from pathlib import Path

from Features.PageObjects.BasePage import BasePage
from Utilities import Controller as con
from Utilities.ReadConfig import readConfig as rc


class ContactUsPage(BasePage):
    # Section name from config.ini file
    section = "CONTACT_US_PAGE"

    def __init__(self,page):
        super().__init__(page)

    def contact_us_enter_name(self, name=None):
        if name is None:
            name = con.get_random_text(8)
        self.type_in(self.section, "contact_us_name_input_field_css", name)
        return name

    def contact_us_enter_email(self,email=None):
        if email is None:
            email = f"{con.get_cur_dt()}_{con.get_cur_time()}@yopmail.com"
        self.type_in(self.section, "contact_us_email_input_field_css", email)
        return email

    def contact_us_enter_subject(self, subject=None):
        if subject is None:
            subject = con.get_random_text(10)
        self.type_in(self.section, "contact_us_subject_input_field_css", subject)
        return subject

    def contact_us_enter_message(self, msg=None):
        if msg is None:
            msg = con.get_random_text(10)
        self.type_in(self.section, "contact_us_msg_input_field_css", msg)
        return msg

    def contact_us_upload_file(self, file_path=None):
        if file_path is None:
            file_path = os.path.join(str(Path.cwd()), "TestData", "Documents", "dummy.pdf")
        self.page.locator(rc(self.section, "contact_us_upload_file_input_field_css")).set_input_files(file_path)

    def click_contact_us_submit_btn(self):
        self.do_click(self.section, "contact_us_submit_btn_css")

    def click_contact_us_redirect_home_btn(self):
        self.do_click(self.section, "contact_us_home_redirect_btn_css")