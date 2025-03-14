from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.data import BASE_URL, USERNAME, PASSWORD


class LoginPage(BasePage):
    URL = BASE_URL

    # Locators
    USERNAME_INPUT = By.XPATH, '//input[@data-test="username"]'
    PASSWORD_INPUT = By.XPATH, '//input[@data-test="password"]'
    LOGIN_BUTTON = By.XPATH, '//input[@data-test="login-button"]'

    # Actions
    def open(self):
        self.driver.get(self.URL)

    def login(self):
        self.enter_text(self.USERNAME_INPUT, USERNAME)
        self.enter_text(self.PASSWORD_INPUT, PASSWORD)
        self.click(self.LOGIN_BUTTON)
