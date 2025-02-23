from pages.complete_page import CompletePage
from pages.information_page import InformationPage
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage
from pages.products_page import ProductsPage
from pages.your_card_page import YourCardPage


def test_buy_backpack_success(driver):
    login_page = LoginPage(driver)
    product_page = ProductsPage(driver)
    card_page = YourCardPage(driver)
    information_page = InformationPage(driver)
    overview_page = OverviewPage(driver)
    complete_page = CompletePage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.successes_login("standard_user","secret_sauce")
    product_page.click_add_product_by_bucket("Sauce Labs Backpack")
    product_page.click_to_basket()
    card_page.click_to_checkout_button()
    information_page.enter_first_name("Slava")
    information_page.enter_last_name("Petrov")
    information_page.enter_zip("222333")
    information_page.click_to_continue()
    overview_page.click_to_finish_button()
    assert complete_page.get_text_complete_message() == "Thank you for your order!"



