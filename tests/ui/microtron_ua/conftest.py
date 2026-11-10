import pytest
from playwright.sync_api import sync_playwright


### Parametrize browsers via params
# @pytest.fixture(scope="module", params=['chromium', 'firefox'])
@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        # browser = getattr(p, request.param).launch(headless=False, slow_mo=100, timeout=10 * 1000)
        browser = p.chromium.launch(headless=False, slow_mo=100, timeout=10 * 1000)
        yield browser
