from core.ui.microtron_ua.locators.main_page import MainPageLocators
from core.ui.microtron_ua.pages.base_page import BasePage
from definitions import MICROTRON_BASE_URL
from logging import getLogger

import time

logger = getLogger()

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page, base_url=MICROTRON_BASE_URL)
        self.url_path = ''
        self.locators = MainPageLocators

    def is_main_page_opened(self):
        elements_to_check = {"URL": self.is_url_correct,
                             "Logo": self.is_logo_visible,
                             "Header": self.is_header_visible,
                             "Left menu": self.is_left_menu_visible,
                             "Main section": self.is_main_section_visible,
                             "Footer": self.is_footer_visible
                             }
        failed_checks = []
        for name, check in elements_to_check.items():
            if not check():
                failed_checks.append(name)
        result = True if failed_checks == [] else False
        return result, failed_checks

    def is_logo_visible(self):
        return self.page.locator(self.locators.header_logo_locator).is_visible()

    def is_header_visible(self):
        return self.page.locator(self.locators.page_header_locator).is_visible()

    def is_left_menu_visible(self):
        return self.page.locator(self.locators.left_menu_locator).is_visible()

    def is_main_section_visible(self):
        return self.page.locator(self.locators.main_section_locator).is_visible()

    def is_footer_visible(self):
        return self.page.locator(self.locators.footer_locator).is_visible()

    def is_url_correct(self):
        return self.page.url == MICROTRON_BASE_URL

    def is_cart_currency_uah(self):
        return self.page.locator(self.locators.cart_amount_locator).text_content().split()[1] == '₴'

    def check_cart_default_amount_is_zero(self):
        return self.page.locator(self.locators.cart_amount_locator).text_content().split()[0] == '0'

    def searched_item_names_contain_target_text(self, search_string):
        search_target_words = search_string.split()
        self.page.locator(self.locators.search_field_locator).fill(search_string)
        self.page.locator(self.locators.search_field_locator).press('Enter')
        search_result_card_locators = self.page.locator(self.locators.search_results_locator).all()
        search_result_item_names = [p.locator('//h3').text_content() for p in search_result_card_locators]
        wrong_item_names = []
        result = True
        for item_name in search_result_item_names:
            if not all(word.lower() in item_name.lower() for word in search_target_words):
                wrong_item_names.append(item_name)
                result = False
        return result, wrong_item_names

