from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc

@when(u'I enter username and password')
def step_impl(context):
    context.lp.enter_username()
    context.lp.enter_password()

@when(u'I submit login')
def step_impl(context):
    context.lp.submit_login()

@then(u'I should be successfully logged in')
def step_impl(context):
    expect(context.page.locator(rc("HEADER_NAV_LINKS", "header_logout_nav_link_css"))).to_have_text("Logout")