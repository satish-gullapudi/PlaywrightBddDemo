import os
import time

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con
from behave.api.pending_step import StepNotImplementedError

@when(u'I click Add to Cart button')
def step_impl(context):
    context.page.get_by_role("button", name="Add to cart").click()


@then(u'I should see product has been added confirmation popup')
def step_impl(context):
    expect(context.page.locator("div.modal-content")).to_be_visible()


@when(u'I click on View Cart button')
def step_impl(context):
    context.page.get_by_role("link", name="View Cart").click()
    time.sleep(5)


@then(u'I should navigate to view cart page')
def step_impl(context):
    expected = os.environ.get("BASE_URL") + "view_cart"
    expect(context.page).to_have_url(expected)


@then(u'I should see the product that I added to the cart')
def step_impl(context):
    expect(context.page.locator(f"a:has-text('{context.random_product}')")).to_be_visible()


@when(u'I click cart navigation link in header')
def step_impl(context):
    context.page.locator("li:has-text('Cart')").click()

