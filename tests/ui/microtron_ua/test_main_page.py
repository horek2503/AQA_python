import pytest
import time
import allure
from allure_commons.types import AttachmentType

from core.ui.microtron_ua.pages.main_page import MainPage


@pytest.fixture(scope="function")
def home_page(browser, request):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    home_page = MainPage(context.new_page())
    home_page.open()

    yield home_page

    home_page.page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
    allure.attach.file(f"screenshots/{request.node.name}.png",
                  name='screenshot',
                  attachment_type=AttachmentType.PNG)

    allure.attach.file(f"traces/{request.node.name}.zip",
                       name='trace',
                       attachment_type=AttachmentType.ZIP)
    context.close()

@allure.epic("Microtron project (UI)")
@allure.feature("Microtron main page")
@pytest.mark.ui
@pytest.mark.pom_style
class  TestsUiMicrotronMainPage:

    @allure.story("Main page smoke")
    @pytest.mark.smoke
    def test_microtron_main_page_smoke(self,home_page):
        """Checking that basic page elements are available"""
        page = home_page
        result, failed_checks = page.is_main_page_opened()
        assert result == True, f'Main page is not opened! Failed to load: {failed_checks}'

    @allure.story("Main page smoke")
    @pytest.mark.smoke
    def test_microtron_check_default_cart_currency(self, home_page):
        """Checking default currency"""
        page = home_page
        assert page.is_cart_currency_uah(), 'Cart currency is incorrect!'

    @allure.story("Main page smoke")
    @pytest.mark.smoke
    def test_microtron_check_default_currency_is_zero(self, home_page):
        """Checking default cart amount = 0"""
        page = home_page
        assert page.check_cart_default_amount_is_zero(), 'Cart amount is not 0!'

    @allure.story("Main page search functionality")
    @pytest.mark.parametrize('search_phrase', ['Lenovo legion 5060',
                                               'Asus Rog strix',
                                               'ddr5 32 gb'])
    def test_microtron_search_on_main_page(self,home_page, search_phrase):
        """Checking search functionality on main page"""
        page = home_page
        result, wrong_item_names = page.searched_item_names_contain_target_text(search_phrase)
        time.sleep(3)
        assert result == True, f'Search results are incorrect. Wrong items: {wrong_item_names}'
