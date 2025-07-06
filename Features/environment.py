from datetime import datetime
from pathlib import Path

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from Utilities import ReadConfig as rc
from Utilities.DBManager import DBManager


def before_all(context):
    context.db = DBManager()
    context.playwright = sync_playwright().start()
    browser_type = rc.readConfig("basic_info", "browser")

    if browser_type.lower() == "chrome":
        context.browser = context.playwright.chromium.launch(headless=False, channel="chrome")
    elif browser_type.lower() == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    else:
        raise Exception(f"Unsupported browser: {browser_type}")
    context.environment = "QA"


def before_scenario(context, scenario):
    context.start_time = datetime.now()
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    scenario_name = scenario.name.split("--")[0].strip()
    end_time = datetime.now()
    status = "Passed" if scenario.status == "passed" else "Failed"
    error_message = str(scenario.exception) if scenario.status == "failed" else ""

    screenshot_path = ""
    if scenario.status == "failed":
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        screenshot_file = screenshots_dir / f"{scenario.name.replace(' ', '_')}.png"
        context.page.screenshot(path=str(screenshot_file))
        screenshot_path = str(screenshot_file)

    context.db.log_test_result(
        test_name=scenario_name,
        module=scenario.feature.name,
        status=status,
        start_time=context.start_time,
        end_time = end_time,
        error_message=error_message,
        screenshot_path=screenshot_path,
        browser="chromium",
        environment=context.environment
    )

    context.page.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
    context.db.close()

def after_step(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot,name='screenshot',attachment_type=AttachmentType.PNG)