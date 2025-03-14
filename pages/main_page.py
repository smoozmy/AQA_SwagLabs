from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    # Locators
    TITLE = By.XPATH, '//span[@data-test="title"]'

    # Actions
    def get_title(self):
        return self.get_text(self.TITLE)