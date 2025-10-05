import os

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc

@Given(u'I launch application and go to login page')
def step_impl(context):
    context.page.goto(os.environ.get("BASE_URL"))
    context.header.click_header_login_naav_link()

@when(u'I go to signup page and fill all details')
def step_impl(context):
    context.lp.signup_enter_name()
    context.lp.signup_enter_signup_email()
    context.lp.click_signup_submit_btn()
    context.sp.signup_click_title_checkbox()
    context.sp.signup_enter_password()
    context.sp.signup_select_dob()
    context.sp.click_signup_newsletter_checkbox()
    context.sp.click_special_offers_optin_checkbox()
    context.sp.signup_enter_fname()
    context.sp.signup_enter_lname()
    context.sp.signup_enter_company()
    context.sp.signup_enter_address1()
    context.sp.signup_enter_address2()
    context.sp.signup_select_country()
    context.sp.signup_enter_state()
    context.sp.signup_enter_city()
    context.sp.signup_enter_zipcode()
    context.sp.signup_enter_mobile_number()

@when(u'I submit signup')
def step_impl(context):
    context.sp.click_signup_create_account_submit_btn()

@then(u'New user successfully to be created')
def step_impl(context):
    selector = rc("ACCOUNT_CREATED_PAGE", "account_created_confirmation_text_css")
    expected = "Congratulations! Your new account has been successfully created!"
    expect(context.page.locator(selector)).to_have_text(expected)
