import os
import random

from Features.PageObjects.BasePage import BasePage
from Utilities import Controller as con


class SignupPage(BasePage):
    # Section name from config.ini file
    section = "SIGNUP_PAGE"

    def __init__(self,page):
        super().__init__(page)

    def signup_click_title_checkbox(self, title=None):
        if title is None:
            title = random.choice(["Mr", "Mrs"])
        if title == "Mr":
            self.do_click(self.section, "signup_title_mr_checkbox_css")
        elif title == "Mrs":
            self.do_click(self.section, "signup_title_mrs_checkbox_css")
        return title

    def signup_enter_signup_name(self, signup_name=None):
        if signup_name is None:
            rand_signup_name = con.get_random_text(8)
            self.type_in(self.section, "signup_name_input_field_css", rand_signup_name)
        else:
            self.type_in(self.section, "signup_name_input_field_css", signup_name)
        return signup_name

    def signup_enter_password(self, password=None):
        if password is None:
            password = con.generate_secure_password(8)
        self.type_in(self.section, "signup_password_input_field_css", password)
        return password

    def signup_select_dob(self, dob=None):
        if dob is None:
            dt, month, year = con.get_random_date_components()
        else:
            dt, month, year = dob
        self.select_dropdown_option_by_visible_text(self.section, "signup_dob_days_drp_select_css",dt)
        self.select_dropdown_option_by_visible_text(self.section, "signup_dob_month_drp_select_css", month)
        self.select_dropdown_option_by_visible_text(self.section, "signup_dob_year_drp_select_css", year)
        return dt, month, year

    def click_signup_newsletter_checkbox(self):
        self.get_element(self.section, "signup_newsletter_checkbox_css").check()

    def click_special_offers_optin_checkbox(self):
        self.get_element(self.section, "signup_special_offers_optin_checkbox_css").check()

    def signup_enter_fname(self, fname=None):
        if fname is None:
            fname = con.get_random_text(8)
        self.type_in(self.section, "signup_fname_input_field_css", fname)
        return fname

    def signup_enter_lname(self, lname=None):
        if lname is None:
            lname = con.get_random_text(8)
        self.type_in(self.section, "signup_lname_input_field_css", lname)
        return lname

    def signup_enter_company(self, company=None):
        if company is None:
            company = con.get_random_text(10)
        self.type_in(self.section, "signup_company_input_field_css", company)
        return company

    def signup_enter_address1(self, address1=None):
        if address1 is None:
            address1 = con.get_random_text(10)
        self.type_in(self.section, "signup_address1_input_field_css", address1)
        return address1

    def signup_enter_address2(self, address2=None):
        if address2 is None:
            address2 = con.get_random_text(10)
        self.type_in(self.section, "signup_address2_input_field_css", address2)
        return address2

    def signup_select_country(self,country=None):
        ele = self.get_element(self.section, "signup_country_drp_select_css")
        if country is None:
            option_list = self.get_element(self.section, "signup_country_drp_options_css").all_text_contents()
            country = random.choice(option_list)
        ele.select_option(label=country)
        return country

    def signup_enter_state(self, state=None):
        if state is None:
            state = con.get_random_text(8)
        self.type_in(self.section, "signup_state_input_field_css", state)
        return state

    def signup_enter_city(self, city=None):
        if city is None:
            city = con.get_random_text(8)
        self.type_in(self.section, "signup_city_input_field_css", city)
        return city

    def signup_enter_zipcode(self, zipcode=None):
        if zipcode is None:
            zipcode = con.get_random_text(8)
        self.type_in(self.section, "signup_zipcode_input_field_css", zipcode)
        return zipcode

    def signup_enter_mobile_number(self, mobile_number=None):
        if mobile_number is None:
            mobile_number = random.randint(1234567890, 9999999999)
        self.type_in(self.section, "signup_mobile_number_input_field_css", str(mobile_number))
        return mobile_number

    def click_signup_create_account_submit_btn(self):
        self.do_click(self.section, "signup_create_account_submit_btn_css")

    def click_account_created_page_continue_btn(self):
        self.do_click("ACCOUNT_CREATED_PAGE", "account_created_continue_btn_css")