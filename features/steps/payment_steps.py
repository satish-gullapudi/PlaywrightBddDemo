import random

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con


@when(u'I enter payment details like Name on Card, Card Number, CVC, Expiration date')
def step_impl(context):
    name_on_card = con.get_random_text(10)
    card_number = str(random.randint(111111111111, 999999999999))
    cvc_number = str(random.randint(111, 999))
    expiration_month = str(random.randint(1, 12))
    expiration_year = str(random.randint(2030, 2040))
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_name_on_card_field_css")).fill(name_on_card)
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_card_number_field_css")).fill(card_number)
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_cvc_field_css")).fill(cvc_number)
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_expiration_month_field_css")).fill(expiration_month)
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_expiration_year_field_css")).fill(expiration_year)

@when(u'I Click Pay and Confirm Order button')
def step_impl(context):
    context.page.locator(rc("PAYMENT_PAGE", "payment_page_pay_and_confirm_btn_css")).click()

@then(u'Verify order confirmation message')
def step_impl(context):
    expect(context.page.get_by_text("Congratulations! Your order has been confirmed!", exact=True)).to_be_visible()