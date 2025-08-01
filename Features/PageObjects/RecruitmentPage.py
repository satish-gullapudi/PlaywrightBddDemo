from Features.PageObjects.BasePage import BasePage
import Utilities.Locators as loc


class RecruitmentPage(BasePage):
    section = "login_page"

    def __init__(self,page):
        super().__init__(page)

    def click_side_panel_recruitment_nav_link(self):
        self.do_click(loc.get_side_panel_recruitment_nav_link_locator())

    def click_recruitment_pg_add_new_candidate_btn(self):
        self.do_click(loc.get_recruitment_pg_add_new_candidate_btn_locator())

    def click_recruitment_pg_add_new_candidate_vacancy_dropdown(self):
        self.do_click(loc.get_recruitment_pg_add_new_candidate_vacancy_dropdown_locator())

    def get_list_of_available_recruitment_vacancy_options(self):
        opt_elements = self.page.locator(
            loc.get_recruitment_pg_add_new_candidate_vacancy_dropdown_options_locator()).all()
        return [option.text_content() for option in opt_elements]