from behave import *

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con


@then(u'Verify Address Details and Review Your Order')
def step_impl(context):
    address_box = context.page.locator(rc("CHECKOUT_PAGE", "checkout_page_your_delivery_address_container_css"))

    # Note: .inner_text() helps clean up extra whitespace
    actual_text = address_box.inner_text()

    # Assertions
    assert context.test_signup_data.get("address1") in actual_text
    assert context.test_signup_data.get("address2") in actual_text
    assert context.test_signup_data.get("city") in actual_text
    assert context.test_signup_data.get("state") in actual_text
    assert context.test_signup_data.get("zipcode") in actual_text
    assert context.test_signup_data.get("country") in actual_text
    assert context.test_signup_data.get("phone") in actual_text

@when(u'I Enter description in comment text area')
def step_impl(context):
    rand_text = con.get_random_text(30)
    context.page.locator(rc("CHECKOUT_PAGE", "checkout_page_add_comment_textarea_css")).fill(rand_text)

@when(u'Click Place Order CTA')
def step_impl(context):
    context.page.locator(rc("CHECKOUT_PAGE", "checkout_page_place_order_btn_css")).click()