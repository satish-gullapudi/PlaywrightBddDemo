from behave import *
from playwright.sync_api import expect


@then(u'"{product1}" and "{product2}" are added to Cart')
def step_impl(context, product1, product2):
    expect(context.page.get_by_role("link", name=product1)).to_be_visible()
    expect(context.page.get_by_role("link", name=product2)).to_be_visible()

@then(u'Their prices, quantity and total price are correct')
def step_impl(context):
    expect(context.page.locator(".cart_quantity > .disabled").nth(0)).to_have_text("1")
    expect(context.page.locator(".cart_price > *").nth(0)).to_have_text(context.raw_price1)
    expect(context.page.locator("p.cart_total_price").nth(0)).to_have_text(context.raw_price1)

    expect(context.page.locator(".cart_quantity > .disabled").nth(1)).to_have_text("1")
    expect(context.page.locator(".cart_price > *").nth(1)).to_have_text(context.raw_price2)
    expect(context.page.locator("p.cart_total_price").nth(1)).to_have_text(context.raw_price2)

@when(u'I increase product quantity to 4')
def step_impl(context):
    context.page.locator("#quantity").focus()

    # Press ArrowUp 3 times to change the value from 1 to 4
    for _ in range(3):
        context.page.keyboard.press("ArrowUp")


@then(u'Product price, quantity, and total quantity should be correct')
def step_impl(context):
    total_price = context.clean_prod_price * 4
    expect(context.page.locator(".cart_price > *").nth(0)).to_have_text(context.raw_prod_price)
    expect(context.page.locator(".cart_quantity > .disabled").nth(0)).to_have_text("4")
    expect(context.page.locator("p.cart_total_price").nth(0)).to_have_text(f"Rs. {total_price}")