import allure
from page_objects.base_page import BasePage
from locators.login_locators import LoginLocators
from constants import Constants


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Тап на на кнопку "Восстановить пароль"')
    def click_password_recovery(self):
        element = self.driver.find_element(*LoginLocators.BUTTON_RECOVERY)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод почты в инпут и тап на кнопку "Вoсстановить"')
    def send_keys_input_email(self):
        self.driver.find_element(*LoginLocators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        element = self.driver.find_element(*LoginLocators.BTN_RECOVERY)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод пароля в инпут')
    def send_keys_input_password(self):
        self.driver.find_element(*LoginLocators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)

    @allure.step('Тапает на иконку глаза, для просмотра введенного пароля')
    def tap_password_icon_eye(self):
        element = self.driver.find_element(*LoginLocators.ICON_EYE)
        self.driver.execute_script("arguments[0].click();", element)
