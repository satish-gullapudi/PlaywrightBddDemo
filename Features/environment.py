import os
import time
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

    # Create a directory for videos if it doesn't exist
    context.video_dir = Path("Reports")
    context.video_dir.mkdir(parents=True, exist_ok=True)

    if browser_type.lower() == "chrome":
        context.browser = context.playwright.chromium.launch(headless=True,
                                                             channel="chrome",
                                                             slow_mo=500  # Milliseconds
                                                             )
    elif browser_type.lower() == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    else:
        raise Exception(f"Unsupported browser: {browser_type}")
    context.environment = "QA"


def before_scenario(context, scenario):
    context.start_time = datetime.now()

    # Define the video path based on the scenario name
    # Sanitize scenario name for valid filename
    sanitized_scenario_name = "".join(c for c in scenario.name if c.isalnum() or c in (' ', '.', '_')).replace(' ', '_')
    context.scenario_video_path = context.video_dir / f"{sanitized_scenario_name}.webm"

    context.browser = context.browser.new_context(
        record_video_dir=context.video_dir,
        record_video_size={"width": 1280, "height": 720},  # Recommended size
        viewport={"width": 1280, "height": 720},
    )
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
    time.sleep(2)

    # Get the actual video path from Playwright after the context is closed
    # Playwright might append a hash to the filename
    video_file_path = context.page.video.path() if context.page.video else None

    if video_file_path and os.path.exists(video_file_path):
        # If Playwright generated a different name, rename it to our desired name
        # This makes sure the file name is clean and readable for the scenario
        try:
            os.rename(video_file_path, context.scenario_video_path)
            print(f"Video saved for scenario '{scenario.name}': {context.scenario_video_path.resolve()}")
        except OSError as e:
            print(f"Error renaming video for '{scenario.name}': {e}")
            print(f"Original video path: {video_file_path}")
            print(f"Desired video path: {context.scenario_video_path}")
    else:
        print(f"No video generated or found for scenario '{scenario.name}'.")


def after_all(context):
    context.browser.close()
    context.playwright.stop()
    context.db.close()

def after_step(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot,name='screenshot',attachment_type=AttachmentType.PNG)