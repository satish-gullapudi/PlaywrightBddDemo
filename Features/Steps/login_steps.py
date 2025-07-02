import time

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Features.PageObjects.LoginPage import LoginPage
import Utilities.Locators as loc


@given(u'I navigate to OrangeHRM')
def step_impl(context):
    context.login = LoginPage(context.page)
    context.page.goto(rc("basic_info", "url"))

@when(u'I enter "{username}" and "{password}"')
def step_impl(context,username, password):
    context.login.enter_username(username)
    context.login.enter_password(password)

@when(u'I submit login')
def step_impl(context):
    context.login.submit_login()
    time.sleep(3)

@then(u'I should see dashboard')
def step_impl(context):
    expected = loc.get_dashboard_url()
    expect(context.page).to_have_url(expected)

@when(u'I click logout')
def step_impl(context):
    pass

@then(u'I should go to login page')
def step_impl(context):
    pass
