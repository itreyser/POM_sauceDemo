from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    BASKET_LOCATOR = (By.CLASS_NAME, "shopping_cart_link")
    ALL_PRODUCT_LOCATOR = '//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]'
    ADD_TO_CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")

    def get_product_by_name(self, product_name):
        locator = self.ALL_PRODUCT_LOCATOR.format(product_name=product_name)
        return self.find_element((By.XPATH, locator))

    def click_add_product_by_bucket(self, product_name):
        product_element = self.get_product_by_name(product_name)
        if not product_element:
            raise ValueError(f"Товар '{product_name}' не найден!")
        self.find_element(self.ADD_TO_CARD_BUTTON_LOCATOR).click()

    def click_to_basket(self):
        self.find_element(self.BASKET_LOCATOR).click()
