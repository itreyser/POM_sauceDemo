from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_card_page import YourCardPage


def test_add_product_to_card(driver):
    login_page = LoginPage(driver)
    product_page = ProductsPage(driver)
    card = YourCardPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.successes_login("standard_user","secret_sauce")
    product_page.click_add_product_by_bucket("Sauce Labs Backpack")
    product_page.click_to_basket()
    assert card.product_in_card("Sauce Labs Backpack") == True

