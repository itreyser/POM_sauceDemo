from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CompletePage(BasePage):
    COMPLETE_MESSAGE = (By.CSS_SELECTOR, "h2[data-test=complete-header]")

    def get_text_complete_message(self):
        return self.find_element(self.COMPLETE_MESSAGE).text
