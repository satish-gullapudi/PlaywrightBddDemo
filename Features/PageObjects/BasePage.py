from Utilities.ReadConfig import readConfig as rc
import logging
import allure

from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class BasePage:

    def __init__(self,page):
        self.page = page

    def do_click(self, locator):
        with allure.step(f"Clicking on an Element {locator}"):
          self.page.locator(locator).click()
          log.logger.info(f"Clicking on an Element {locator}")

    def type(self, locator, value):
        with allure.step(f"Typing in an Element {locator} and entered value as {value}"):
          self.page.locator(locator).fill(value)
          log.logger.info(f"Typing in an Element {locator} and entered value as {value}")

    def move_to(self, locator):
        with allure.step(f"Moving to an Element {locator}"):
          self.page.locator(locator).hover()
          log.logger.info(f"Moving to an Element {locator}")


    def select(self, locator, value):
        with allure.step(f"Selecting from an Element {locator} and selected value as {value}"):
          self.page.select_option(locator,value)
          log.logger.info(f"Selecting from an Element {locator} and selected value as {value}")