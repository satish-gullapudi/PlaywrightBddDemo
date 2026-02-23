import allure
from allure_commons.types import AttachmentType

from Utilities.ReadConfig import readConfig as rc

class BasePage:

    def __init__(self,page):
        self.page = page
        self.get_element = lambda section, key:self.page.locator(rc(section, key))
        self.do_click = lambda section, key:self.page.locator(rc(section, key)).click()
        self.type_in = lambda section, key, value:self.page.locator(rc(section, key)).fill(value)

    def select_dropdown_option_by_visible_text(self, section, key, visible_text):
        ele = self.get_element(section, key)
        ele.select_option(label=visible_text)

    def handle_and_accept_alert(self, dialog):
        """
        This function is called when a dialog appears.
        """
        dialog.accept()

    def take_screenshot(self, screenshot_name=None):
        # Attaches screenshot to allure after every step
        if screenshot_name is None:
            screenshot_name='screenshot'
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=screenshot_name, attachment_type=AttachmentType.PNG)