import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from Utilities import ReadConfig as rc


def before_scenario(context,scenario):
    context.playwright = sync_playwright().start()
    browser_type = rc.readConfig("basic_info","browser")

    if browser_type.lower() == "chrome":
        context.browser = context.playwright.chromium.launch(headless=False,channel="chrome")
    elif browser_type.lower() == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    else:
        raise Exception(f"Unsupported browser: {browser_type}")

    context.page = context.browser.new_page()



def after_scenario(context,scenario):
    context.page.close()
    context.browser.close()
    context.playwright.stop()


def after_step(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot,name='screenshot',attachment_type=AttachmentType.PNG)