import allure

from locators.login_locators import LoginLocators
from constants import Constants


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Авторизация пользователя')
    def login_personal_account(self):
        self.driver.find_element(*LoginLocators.EMAIL).send_keys(Constants.EMAIL)
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(Constants.PASSWORD)
        element = self.driver.find_element(*LoginLocators.AUTH_BUTTON_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", element)
