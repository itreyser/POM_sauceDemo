from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class YourCardPage(BasePage):
    ALL_PRODUCT_LOCATOR = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def product_in_card(self, product_name):
        list_elements = self.find_elements(self.ALL_PRODUCT_LOCATOR)
        flag = False
        for i in list_elements:
            if i.text == product_name:
                flag = True
        return flag

    def click_to_checkout_button(self):
        self.click_element(self.CHECKOUT_BUTTON)
