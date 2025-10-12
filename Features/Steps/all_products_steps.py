import os

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con

@when(u'Go to all products page')
def step_impl(context):
    context.header.click_header_products_nav_link()

@then(u'I should be navigated to ALL PRODUCTS page successfully')
def step_impl(context):
    expect(context.page.locator(rc(context.products.section, "products_brands_filter_polo_option_link_css"))).to_be_visible()

@then(u'Products list is visible')
def step_impl(context):
    product_name = context.page.locator(rc(context.products.section, "products_individual_card_produce_name_css"))
    expected_product_count = 33
    try:
        expect(product_name).to_have_count(expected_product_count)
    except AssertionError as e:
        context.bp.take_screenshot(f"Expected product count not matches actual")
        context.failed_assertions_count += 1

@when(u'I click on view product of first product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on view product of first product')


@then(u'I should be landed on product detail page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be landed on product detail page')


@then(u'Product detail is visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Product detail is visible')