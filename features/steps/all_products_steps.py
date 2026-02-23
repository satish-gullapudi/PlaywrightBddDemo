import json
import os
import random
import re
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
    context.product_names = context.page.locator(rc(context.products.section, "products_individual_card_produce_name_css")).all_inner_texts()
    expect(product_name).to_have_count(len(context.product_detail_list))

@when(u'I click on view product of first product')
def step_impl(context):
    view_product_cta_locator = rc(context.products.section, "products_individual_card_view_product_cta_css")
    context.page.locator(view_product_cta_locator).first.click()

@when(u'I click on view product of random product')
def step_impl(context):
    context.random_product = random.choice(context.product_names)
    card_label_locator = rc(context.products.section, "products_all_products_cards_list_css")
    view_product_cta_locator = rc(context.products.section, "products_individual_card_view_product_cta_css")
    context.page.locator(card_label_locator).filter(has_text=context.random_product).locator(view_product_cta_locator).click()

@then(u'I should be landed on product detail page')
def step_impl(context):
    expect(context.page.locator('b:has-text("Availability:")')).to_be_visible()
    context.prod_name = context.page.locator("div[class='product-information'] h2").inner_text()
    context.raw_prod_price = context.page.locator("div[class='product-information'] span span").inner_text()
    context.clean_prod_price = int(re.search(r'\d+', context.raw_prod_price).group())

@then(u'Product detail is visible')
def step_impl(context):
    prod_name = context.product_detail_list[0].get("name")
    prod_price = context.product_detail_list[0].get("price")
    prod_brand = context.product_detail_list[0].get("brand")
    expect(context.page.locator(f'h2:has-text("{prod_name}")')).to_be_visible()
    expect(context.page.locator(f"//span[normalize-space()='{prod_price}']")).to_be_visible()
    expect(context.page.locator(f'p:has-text("Brand: {prod_brand}")')).to_be_visible()

@when(u'I hover over and add products "{product1}" and "{product2}" to cart')
def step_impl(context, product1, product2):
    target_card = context.page.locator(rc(context.products.section, "products_all_products_cards_list_css")).filter(has_text=product1)
    target_card.scroll_into_view_if_needed()
    target_card.hover()
    target_card.locator(rc(context.products.section, "products_individual_card_overlay_add_to_cart_cta_css")).click()
    context.page.get_by_role("button", name="Continue Shopping").click()

    price_element = target_card.locator(rc(context.products.section, "products_individual_card_product_price_css"))
    context.raw_price1 = price_element.inner_text()
    import re
    prod1_clean_price = int(re.search(r'\d+', context.raw_price1).group())

    target_card = context.page.locator(rc(context.products.section, "products_all_products_cards_list_css")).filter(has_text=product2)
    target_card.scroll_into_view_if_needed()
    target_card.hover()
    target_card.locator(rc(context.products.section, "products_individual_card_overlay_add_to_cart_cta_css")).click()

    price_element = target_card.locator(rc(context.products.section, "products_individual_card_product_price_css"))
    context.raw_price2 = price_element.inner_text()
    import re
    prod2_clean_price = int(re.search(r'\d+', context.raw_price2).group())