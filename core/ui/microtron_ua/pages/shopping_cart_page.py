import allure
from playwright.sync_api import Page

from core.ui.microtron_ua.locators.shopping_cart_page import ShoppingCartPageLocators
from core.ui.microtron_ua.pages.base_page import BasePage
from definitions import MICROTRON_BASE_URL



class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, base_url=MICROTRON_BASE_URL)
        self.url_path = 'cart'
        self.locators = ShoppingCartPageLocators
        self.page = page

    @allure.step("Checking shopping cart page is opened")
    def is_shopping_cart_page_opened(self):
        elements_to_check = {"URL": self.is_url_correct,
                             "Logo": self.is_logo_visible,
                             "Page name": self.is_page_name_visible,
                             "Go back button": self.is_go_back_button_visible
                             }
        failed_checks = []
        for name, check in elements_to_check.items():
            if not check():
                failed_checks.append(name)
        result = True if failed_checks == [] else False
        return result, failed_checks

    @allure.step("Checking URL is correct")
    def is_url_correct(self):
        return self.page.url == MICROTRON_BASE_URL + self.url_path

    @allure.step("Checking logo is visible")
    def is_logo_visible(self):
        return self.page.locator(self.locators.empty_cart_logo).is_visible()

    @allure.step("Checking page name is correct")
    def is_page_name_visible(self):
        return self.page.locator(self.locators.page_name).is_visible()

    @allure.step("Checking 'go back' button is visible")
    def is_go_back_button_visible(self):
        return self.page.locator(self.locators.page_name).is_visible()
