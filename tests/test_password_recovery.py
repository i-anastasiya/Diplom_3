import allure

from locators.login_locators import LoginLocators
from page_objects.base_page import BasePage
from page_objects.password_recovery_page import PasswordRecoveryPage

class TestStellarBurgersPasswordRecovery:
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery(self, login):
        recovery_page = PasswordRecoveryPage(login)
        recovery_page_1 = BasePage(login)
        recovery_page.click_password_recovery()
        name_button = recovery_page_1.wait_element_visibility_of_element_located_text(LoginLocators.BUTTON_LOGIN)
        assert name_button == 'Войти'

    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_password_recovery_email(self, login):
        recovery_page = PasswordRecoveryPage(login)
        recovery_page.click_password_recovery()
        recovery_page.send_keys_input_email()
        assert login.find_element(*LoginLocators.TITLE_RECOVERY).text == 'Восстановление пароля'

    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_open(self, login):
        recovery_page = PasswordRecoveryPage(login)
        recovery_page.send_keys_input_password()
        recovery_page.tap_password_icon_eye()
        assert login.find_element(*LoginLocators.INPUT_PASSWORD_ACTIVE)
