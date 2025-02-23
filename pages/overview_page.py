from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def click_to_finish_button(self):
        self.click_element(self.FINISH_BUTTON)
