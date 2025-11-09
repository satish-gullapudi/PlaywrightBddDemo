import json
import os
import time

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc

@when(u'Go to all products page')
def step_impl(context):
    context.header.click_header_products_nav_link()

@then(u'I should be navigated to ALL PRODUCTS page successfully')
def step_impl(context):
    expect(context.page.locator(rc(context.products.section, "products_brands_filter_polo_option_link_css"))).to_be_visible()

@then(u'Products list is visible')
def step_impl(context):
    api = os.environ.get("PRODUCT_LIST_API")

    # Opening new tab to get list of products from API
    browser_context = context.page.context
    new_page = browser_context.new_page()
    new_page.goto(api)
    resp = new_page.locator('//body').text_content()
    new_page.close()
    resp = json.loads(resp.strip())
    context.product_detail_list = resp["products"]

    product_name = context.page.locator(rc(context.products.section, "products_individual_card_produce_name_css"))
    expect(product_name).to_have_count(len(context.product_detail_list))

@when(u'I click on view product of first product')
def step_impl(context):
    view_product_cta_locator = rc(context.products.section, "products_individual_card_view_product_cta_css")
    context.page.locator(view_product_cta_locator).first.click()

@then(u'I should be landed on product detail page')
def step_impl(context):
    expect(context.page.locator('b:has-text("Availability:")')).to_be_visible()

@then(u'Product detail is visible')
def step_impl(context):
    prod_name = context.product_detail_list[0].get("name")
    prod_price = context.product_detail_list[0].get("price")
    prod_brand = context.product_detail_list[0].get("brand")
    expect(context.page.locator(f'h2:has-text("{prod_name}")')).to_be_visible()
    expect(context.page.locator(f"//span[normalize-space()='{prod_price}']")).to_be_visible()
    expect(context.page.locator(f'p:has-text("Brand: {prod_brand}")')).to_be_visible()