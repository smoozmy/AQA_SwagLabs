from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login()

        main_page = MainPage(driver)

        assert main_page.get_title() == 'Products'