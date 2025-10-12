import os
import random

from Features.PageObjects.BasePage import BasePage
from Utilities import Controller as con


class AllProducts(BasePage):
    # Section name from config.ini file
    section = "ALL_PRODUCTS_PAGE"

    def __init__(self,page):
        super().__init__(page)

    def enter_text_into_all_products_search_field(self, text):
        self.type_in(self.section, "products_search_field_css", text)

    def click_all_products_submit_search_btn(self):
        self.do_click(self.section, "products_search_field_submit_search_btn_css")

    def click_all_products_women_category_filter_btn(self):
        self.do_click(self.section, "products_category_women_filter_btn_css")

    def get_list_of_options_under_all_products_women_category_filter(self):
        return self.page.locator(self.section, "products_category_women_filter_dropdown_options_css").all()

    def click_all_products_women_category_filter_dropdown_option_by_name(self, sub_category_type=None):
        if sub_category_type.lower() == 'dress':
            self.do_click(self.section, "products_category_women_filter_dress_option_css")
        elif sub_category_type.lower() == 'tops':
            self.do_click(self.section, "products_category_women_filter_tops_option_css")
        elif sub_category_type.lower() == 'saree':
            self.do_click(self.section, "products_category_women_filter_saree_option_css")

    def click_all_products_men_category_filter_btn(self):
        self.do_click(self.section, "products_category_men_filter_btn_css")

    def get_list_of_options_under_all_products_men_category_filter(self):
        return self.page.locator(self.section, "products_category_men_filter_dropdown_options_css").all()

    def click_all_products_men_category_filter_dropdown_option_by_name(self, sub_category_type=None):
        if sub_category_type.lower() == 'tshirts':
            self.do_click(self.section, "products_category_men_filter_tshirts_option_css")
        elif sub_category_type.lower() == 'jeans':
            self.do_click(self.section, "products_category_men_filter_jeans_option_css")

    def click_all_products_kids_category_filter_btn(self):
        self.do_click(self.section, "products_category_kids_filter_btn_css")

    def get_list_of_options_under_all_products_kids_category_filter(self):
        return self.page.locator(self.section, "products_category_kids_filter_dropdown_options_css").all()

    def click_all_products_kids_category_filter_dropdown_option_by_name(self, sub_category_type=None):
        if sub_category_type.lower() == 'tshirts':
            self.do_click(self.section, "products_category_kids_filter_dress_option_css")
        elif sub_category_type.lower() == 'jeans':
            self.do_click(self.section, "products_category_kids_filter_topsnshirts_option_css")

    def get_list_of_all_brands_under_all_products_brands_filter(self):
        return self.page.locator(self.section, "products_brands_filter_list_css").all()

    def click_all_products_brand_filter_option_by_brand_name(self, brand):
        self.page.locator(f".brands-name ul li a:has-text('{brand}')").click()

    def get_all_products_brand_filter_brand_count_by_brand_name(self, brand):
        return self.page.locator(f".brands-name ul li a:has-text('{brand}') span").text_content()