import pytest
import time
import allure


@allure.epic("Microtron project")
@pytest.mark.ui
@pytest.mark.pom_style
class  TestsUiMicrotronMainPage:
    @pytest.mark.smoke
    def test_microtron_main_page_smoke(self,home_page):
        page = home_page
        result, failed_checks = page.is_main_page_opened()
        assert result == True, f'Main page is not opened! Failed to load: {failed_checks}'

    @pytest.mark.smoke
    def test_microtron_check_default_cart_currency(self, home_page):
        page = home_page
        assert page.is_cart_currency_uah(), 'Cart currency is incorrect!'

    @pytest.mark.smoke
    def test_microtron_check_default_currency_is_zero(self, home_page):
        page = home_page
        assert page.check_cart_default_amount_is_zero(), 'Cart amount is not 0!'


    @pytest.mark.parametrize('search_phrase', ['Lenovo legion 5060',
                                               'Asus Rog strix',
                                               'ddr5 32 gb'])
    def test_microtron_search_on_main_page(self,home_page, search_phrase):
        page = home_page
        result, wrong_item_names = page.searched_item_names_contain_target_text(search_phrase)
        time.sleep(3)
        assert result == True, f'Search results are incorrect. Wrong items: {wrong_item_names}'
