import os
import time
from datetime import datetime
from pathlib import Path
import logging
import logging.config

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from Utilities.DBManager import DBManager
from Utilities import Controller as con
from features.PageObjects.BasePage import BasePage
from features.PageObjects.LoginPage import LoginPage
from features.PageObjects.SignupPage import SignupPage
from features.PageObjects.HeaderNav import HeaderNav
from features.PageObjects.ContactUsPage import ContactUsPage
from Utilities.LogUtil import setup_logger
from features.PageObjects.AllProducts import AllProducts

LOG_DIR = 'Logs'

def before_all(context):
    """Setup logging and custom context attributes before the test run."""
    # Ensure the log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)

    context.IS_DOCKER = con.init_env() # Loading environment variables
    BROWSER = os.environ.get("BROWSER")

    # Initiation of DB class which handles storing and fetching tests, test results, etc.
    context.db = DBManager()

    context.playwright = sync_playwright().start()

    # Create a directory for videos if it doesn't exist
    context.video_dir = Path("VideoReports")
    context.video_dir.mkdir(parents=True, exist_ok=True)

    if context.IS_DOCKER:
        headless_mode = True
    else:
        headless_mode = True if os.getenv("HEADLESS") == "True" else False

    if BROWSER.lower() in ("chrome", "chromium"):
        context.browser = context.playwright.chromium.launch(headless=headless_mode,
                                                             slow_mo=500  # Milliseconds
                                                             )
    elif BROWSER.lower() == "firefox":
        context.browser = context.playwright.firefox.launch(headless=True if os.getenv("HEADLESS") == "True" else False)
    else:
        raise Exception(f"Unsupported browser: {BROWSER}")
    context.environment = os.getenv("TESTING_ENVIRONMENT")


def before_scenario(context, scenario):
    context.start_time = datetime.now()

    # Define the video path based on the scenario name and sanitize filename
    sanitized_scenario_name = "".join(c for c in scenario.name if c.isalnum() or c in (' ', '.', '_')).replace(' ', '_')
    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    filename = f"{sanitized_scenario_name}_{timestamp}.webm"
    context.scenario_video_path = context.video_dir / filename

    # Create the unique log file path
    log_file_path = os.path.join(LOG_DIR, f"{sanitized_scenario_name}.log")

    # Configure the logger for this specific file path
    context.logger = setup_logger(log_file_path)

    context.logger.info("-" * 50)
    context.logger.info(f"STARTING SCENARIO: {scenario.name}")

    context.browser = context.browser.new_context(
        ignore_https_errors=True if context.IS_DOCKER else False,
        record_video_dir=context.video_dir,
        record_video_size={"width": 1280, "height": 720},  # Recommended size
        viewport={"width": 1280, "height": 720},
    )
    # Start tracing before creating / navigating a page.
    context.browser.tracing.start(screenshots=True, snapshots=True, sources=True)

    context.page = context.browser.new_page()

    con.block_ads(context.page)

    context.bp = BasePage(context.page)
    context.lp = LoginPage(context.page)
    context.sp = SignupPage(context.page)
    context.header = HeaderNav(context.page)
    context.contact = ContactUsPage(context.page)
    context.products = AllProducts(context.page)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Check if the Playwright page object is available in the context
        if 'page' in context:
            # Capture the screenshot as bytes
            screenshot_bytes = context.page.screenshot()

            # Attach the screenshot to the Allure report
            allure.attach(
                screenshot_bytes,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )

    # Stop tracing and export it into a zip archive.
    context.browser.tracing.stop(path="trace.zip")

    scenario_name = scenario.name.split("--")[0].strip()
    end_time = datetime.now()
    status = "Passed" if scenario.status == "passed" else "Failed"
    error_message = str(scenario.exception) if scenario.status == "failed" else ""

    context.db.log_test_result(
        test_name=scenario_name,
        module=scenario.feature.name,
        status=status,
        start_time=context.start_time,
        end_time = end_time,
        error_message=error_message,
        browser="chromium",
        environment=context.environment
    )

    # Capture the path before closing anything
    temp_video_path = context.page.video.path() if context.page.video else None

    # Close the page and browser context FIRST
    # This ensures Playwright flushes the video buffer to the disk
    context.page.close()
    context.browser.close()

    # Use the finalized file for Allure and Renaming
    if temp_video_path and os.path.exists(temp_video_path):
        # Attach to Allure using the actual file that exists
        allure.attach.file(
            temp_video_path,
            name=f"{scenario.name} Video",
            attachment_type=AttachmentType.WEBM
        )

        # Now rename it for "VideoReports" folder if desired
        try:
            # Note: After renaming, the file moves from temp_video_path to context.scenario_video_path
            os.rename(temp_video_path, context.scenario_video_path)
            context.logger.info(f"Video saved and attached: {context.scenario_video_path}")
        except OSError as e:
            context.logger.info(f"Rename failed, but attachment should have worked: {e}")
    else:
        context.logger.info(f"No video found at {temp_video_path}")

    # Log the scenario status
    context.logger.info(f"SCENARIO FINISHED. {scenario.status}")
    context.logger.info("-" * 50)

    # Crucial step: Close the file handler to ensure the log file is fully written
    # and not locked before the next scenario reconfigures the logger.
    for handler in context.logger.handlers:
        if isinstance(handler, logging.handlers.RotatingFileHandler):
            handler.close()
            context.logger.removeHandler(handler)


def after_all(context):
    """Cleanup after the test run."""
    context.playwright.stop()
    context.db.close()

def after_step(context, step):
    # Attaches screenshot to allure after every step
    screenshot = context.page.screenshot()
    allure.attach(screenshot, name='screenshot', attachment_type=AttachmentType.PNG)