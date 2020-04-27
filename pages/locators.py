from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
