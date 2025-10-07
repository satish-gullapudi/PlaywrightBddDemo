from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con

@when(u'I enter username and password')
def step_impl(context):
    context.lp.enter_username()
    context.lp.enter_password()

@when(u'I enter invalid username and password')
def step_impl(context):
    rand_email = f"{con.get_cur_dt()}_{con.get_cur_time()}@yopmail.com"
    password = con.generate_secure_password(8)
    context.lp.enter_username(rand_email)
    context.lp.enter_password(password)

@when(u'I submit login')
def step_impl(context):
    context.lp.submit_login()

@then(u'I should be successfully logged in')
def step_impl(context):
    expect(context.page.locator(rc("HEADER_NAV_LINKS", "header_logout_nav_link_css"))).to_have_text("Logout")

@then(u'I should see invalid user error message')
def step_impl(context):
    (expect(context.page.locator(rc(context.lp.section, "login_invalid_user_err_msg_css")))
     .to_have_text("Your email or password is incorrect!"))