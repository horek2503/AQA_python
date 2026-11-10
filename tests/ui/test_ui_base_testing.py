import time
import pytest
from assertpy import assert_that, soft_assertions
from playwright.sync_api import sync_playwright, expect
from definitions import SCREEN_FOLDER

#
# def test_any_page_for_demo():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=100, timeout=10000)
#         page = browser.new_page()
#         page.set_default_timeout(5 * 1000)
#         page.goto("https://microtron.ua/")
#         search_phrase = 'Lenovo legion RTX5070'
#
#         # WORK WITH MOUSE SCROLL
#         # page.mouse.wheel(0, 1000)
#         # page.wait_for_timeout(3000)
#         # page.mouse.wheel(0, -500)
#         # page.wait_for_timeout(3000)
#
#         print(page.url)
#         search_locator = page.locator('//div[@class="header_bottom_search_block"]//input[@class="search"]')
#         search_locator.click()
#         search_locator.fill(search_phrase)
#         search_locator.press('Enter')
#
#         searched_url = page.url
#         keywords = search_phrase.split(' ')
#         for keyword in keywords:
#             with soft_assertions():
#                 assert_that(searched_url).contains(keyword)
#
#         page.screenshot(path=f"{SCREEN_FOLDER}/microtron_legion_5070.jpg")
#
#         results_page_locators = page.locator('//div[@class="product_card "]').all()
#         assert len(results_page_locators) == 2, f'2 Results expected, but got {len(results_page_locators)}'
#
#         # taking prices for each card in product card list
#         for product_card in results_page_locators:
#             price_locator = product_card.locator('//p[@class="price_new"]')
#             price_value = ''.join(price_locator.text_content().split(' ')[:-1]) # cut off currency text
#             # print(f'\n{price_value}')
#             assert int(price_value) > 100000, 'Price value is suspiciously low'
#
#         # WORK WITH CHECKBOX
#         checkbox_locator = page.locator('//input[@id="developer-сс9"]')
#         print(checkbox_locator.is_checked())
#         assert checkbox_locator.is_checked() == False, 'Checkbox is expected to be unchecked'
#         checkbox_locator.set_checked(checked=True)
#         print(checkbox_locator.is_checked())
#         assert checkbox_locator.is_checked() == True, 'Checkbox is expected to be checked'
#
#
#         # results_page_locator.click()
#         # print(results_page_locator)
#         page.wait_for_timeout(5 * 1000)
#
# @pytest.fixture(scope="session")
# def home_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=100, timeout=10 * 1000)
#         page = browser.new_page()
#         page.goto("https://microtron.ua/")
#         yield page
#
# @pytest.mark.deprecated
# def test_home_page_is_opened_microtron(home_page):
#     page = home_page
#     page_header_locator = page.locator('//div[@class="header_center"]')
#     header_logo_locator = page_header_locator.get_by_role("img", name="logo")
#
#     with soft_assertions():
#         assert_that(page.url,
#                     f"Expected URL 'https://microtron.ua2/', but got '{page.url}'"
#                     ).is_equal_to("https://microtron.ua/")
#         assert_that(page_header_locator.is_visible(), f'Top menu is not visible').is_true()
#         assert_that(header_logo_locator.is_visible(), f'Favicon is not visible').is_true()
#
# @pytest.mark.deprecated
# def test_cart_amount_value_microtron(home_page, expected_amount=0 ):
#         page = home_page
#         cart_sum_locator = page.locator('div.summ span')
#         cart_amount = int(cart_sum_locator.text_content().split()[0])
#         assert(cart_amount == expected_amount), f'Cart amount expected: {expected_amount}, but got {cart_amount}'
#
#
# def test_for_test_microtron():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=100, timeout=10*1000)
#         page = browser.new_page()
#         page.goto("https://microtron.ua/")

        ### To show locators can be saved and then included locators can be searched inside
        # page_header_locator = page.locator('//div[@class="header_center"]')
        # header_logo_locator = page_header_locator.get_by_role("img", name="logo")
        # # favicon
        # expect(header_logo_locator).to_be_visible()
        # # top menu first section
        # top_menu_locator = page_header_locator.get_by_text("АКЦІЇ")
        # expect(top_menu_locator).to_be_visible()

        ### Locators by CSS
        # login_buton_locator = page.locator("a[class ='profile_non_auth_button uppercase']")
        # expect(login_buton_locator).to_be_visible()
        # # login_buton_locator.click()
        # wishlist_button_locator = page.locator('[href="https://microtron.ua/wishlst"].icon_cont')
        # expect(wishlist_button_locator).to_be_visible()
        # wishlist_button_locator.click()
        # close_sign_in_locator = page.locator('.sign_in_close')
        # close_sign_in_locator.click()

        # time.sleep(5)
