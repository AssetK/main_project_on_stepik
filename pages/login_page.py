from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is presented!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login form is presented!"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True


