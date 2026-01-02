import os
import re

from behave import *
from playwright.sync_api import sync_playwright, expect

@given('I navigate to the "{page_name}"')
def step_impl(context, page_name):
    if page_name == "Home":
        # Check for home page specific element
        expect(context.page.locator("//div[@id='slider-carousel']//div[@class='carousel-inner']")).to_be_visible()
    elif page_name == "Cart":
        # Specific step for cart navigation
        context.execute_steps('When I click cart navigation link in header')

@then(u'I should see carousel slider in home page')
def step_impl(context):
    expect(context.page.locator("//div[@id='slider-carousel']//div[@class='carousel-inner']")).to_be_visible()


@when(u'I scroll down to footer')
def step_impl(context):
    context.page.get_by_role("textbox", name="Your email address").scroll_into_view_if_needed()


@then(u'I should see subscription section')
def step_impl(context):
    expect(context.page.get_by_role("heading", name="Subscription")).to_be_visible()


@when(u'I enter "{email}" in subscription email input box')
def step_impl(context, email):
    context.page.get_by_role("textbox", name="Your email address").fill(email)


@when(u'Click Subscription field arrow button')
def step_impl(context):
    context.page.locator("#subscribe").click()

@then(u'I should see subscription success message')
def step_impl(context):
    expect(context.page.get_by_text("You have been successfully subscribed!", exact=True)).to_be_visible()

    success_msg = context.page.locator("#success-subscribe")
    # Assert that the class attribute does NOT contain "hide"
    # The \b ensures we match the exact word 'hide'
    expect(success_msg).not_to_have_class(re.compile(r"\bhide\b"))