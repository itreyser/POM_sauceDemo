from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InformationPage(BasePage):
    F_NAME_INPUT = (By.ID, "first-name")
    L_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def enter_first_name(self, name):
        self.enter_text(self.F_NAME_INPUT, name)

    def enter_last_name(self, name):
        self.enter_text(self.L_NAME_INPUT, name)

    def enter_zip(self, zip_code):
        self.enter_text(self.ZIP_INPUT, zip_code)

    def click_to_continue(self):
        self.click_element(self.CONTINUE_BUTTON)
