import time

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Features.PageObjects.LoginPage import LoginPage
import Utilities.Locators as loc
from Features.PageObjects.RecruitmentPage import RecruitmentPage

@when(u'I go to Recruitment module')
def step_impl(context):
    context.recruitment = RecruitmentPage(context.page)
    context.recruitment.click_side_panel_recruitment_nav_link()

@when(u'I create new candidate')
def step_impl(context):
    context.recruitment.click_recruitment_pg_add_new_candidate_btn()
    time.sleep(3)
    context.recruitment.click_recruitment_pg_add_new_candidate_vacancy_dropdown()
    options = context.recruitment.get_list_of_available_recruitment_vacancy_options()
    print(options)

@then(u'Candidate should be displayed in recruitment dashboard')
def step_impl(context):
    pass