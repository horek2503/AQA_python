import pytest
import allure
from allure_commons.types import AttachmentType

from core.ui.microtron_ua.pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture(scope="function")
def cart_page(browser, request):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page = ShoppingCartPage(context.new_page())
    page.open()

    yield page

    page.page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    context.tracing.stop(path=f"traces/{request.node.name}.zip")

    allure.attach.file(f"screenshots/{request.node.name}.png",
                  name='screenshot',
                  attachment_type=AttachmentType.PNG)

    allure.attach.file(f"traces/{request.node.name}.zip",
                       name='trace',
                       attachment_type=AttachmentType.ZIP)

    context.close()

@allure.epic("Microtron project (UI)")
@allure.feature("Microtron shopping cart page")
@pytest.mark.ui
@pytest.mark.pom_style
class  TestsUiMicrotronShoppingCartPage:

    @allure.story("Shopping cart page smoke")
    @pytest.mark.smoke
    def test_microtron_shopping_cart_page_smoke(self,cart_page):
        """Checking that shopping cart page elements are available"""
        page = cart_page
        result, failed_checks = page.is_shopping_cart_page_opened()
        assert result == True, f'Main page is not opened! Failed to load: {failed_checks}'
