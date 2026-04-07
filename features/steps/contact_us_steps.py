import time

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc

@when(u'I go to contact us page')
def step_impl(context):
    context.header.click_header_contact_us_nav_link()

@then(u'Get in touch text is visible')
def step_impl(context):
    expect(context.page.locator(rc(context.contact.section, "contact_us_get_in_touch_css"))).to_be_visible()

@when(u'I fill contact us form')
def step_impl(context):
    context.contact.contact_us_enter_name()
    context.contact.contact_us_enter_email()
    context.contact.contact_us_enter_subject()
    context.contact.contact_us_enter_message()

@when(u'I upload file')
def step_impl(context):
    context.contact.contact_us_upload_file()

@when(u'I submit contact us form')
def step_impl(context):
    context.page.on("dialog", context.bp.handle_and_accept_alert)
    context.contact.click_contact_us_submit_btn()

@then(u'I should see success message')
def step_impl(context):
    (expect(context.page.locator(rc(context.contact.section, "contact_us_success_msg_css")))
     .to_have_text("Success! Your details have been submitted successfully."))

@when(u'I click home button')
def step_impl(context):
    context.contact.click_contact_us_redirect_home_btn()

@then(u'I should land on home page')
def step_impl(context):
    expect(context.page.locator(rc(context.contact.section, "contact_us_get_in_touch_css"))).not_to_be_visible()