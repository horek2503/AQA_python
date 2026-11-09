import pytest
from playwright.sync_api import sync_playwright
from core.ui.microtron_ua.pages.main_page import MainPage


### Parametrize browsers via params
# @pytest.fixture(scope="module", params=['chromium', 'firefox'])
@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        # browser = getattr(p, request.param).launch(headless=False, slow_mo=100, timeout=10 * 1000)
        browser = p.chromium.launch(headless=False, slow_mo=100, timeout=10 * 1000)
        yield browser


# @pytest.fixture(scope="session")
# def page(browser):
#     page = browser.new_page()
#     yield page


@pytest.fixture(scope="function")
def home_page(browser, request):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    home_page = MainPage(context.new_page())
    home_page.open()

    yield home_page

    # home_page.page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
    context.close()
