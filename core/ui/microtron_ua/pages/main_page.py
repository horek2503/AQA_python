from playwright.sync_api import Page

from core.ui.microtron_ua.locators.main_page import MainPageLocators
from core.ui.microtron_ua.pages.base_page import BasePage
from core.ui.microtron_ua.pages.shopping_cart_page import ShoppingCartPage
from definitions import MICROTRON_BASE_URL
from logging import getLogger
import allure

logger = getLogger()

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=MICROTRON_BASE_URL)
        self.url_path = ''
        self.locators = MainPageLocators
        self.page = page

    @allure.step("Checking main page is opened")
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

    @allure.step("Checking logo is visible")
    def is_logo_visible(self):
        return self.page.locator(self.locators.header_logo_locator).is_visible()

    @allure.step("Checking header is visible")
    def is_header_visible(self):
        return self.page.locator(self.locators.page_header_locator).is_visible()

    @allure.step("Checking left menu is visible")
    def is_left_menu_visible(self):
        return self.page.locator(self.locators.left_menu_locator).is_visible()

    @allure.step("Checking main section is visible")
    def is_main_section_visible(self):
        return self.page.locator(self.locators.main_section_locator).is_visible()

    @allure.step("Checking footer is visible")
    def is_footer_visible(self):
        return self.page.locator(self.locators.footer_locator).is_visible()

    @allure.step("Checking URL is correct")
    def is_url_correct(self):
        return self.page.url == MICROTRON_BASE_URL

    @allure.step("Checking cart currency is UAH")
    def is_cart_currency_uah(self):
        return self.page.locator(self.locators.cart_amount_locator).text_content().split()[1] == '₴'

    @allure.step("Checking cart currency default amount = 0")
    def check_cart_default_amount_is_zero(self):
        return self.page.locator(self.locators.cart_amount_locator).text_content().split()[0] == '0'

    @allure.step("Checking search results are correct")
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

    def open_shopping_cart_page(self) -> ShoppingCartPage:
        self.page.locator(self.locators.cart_button_locator).click()
        return ShoppingCartPage()

