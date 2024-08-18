import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from page_objects.password_recovery_page import PasswordRecoveryPage

class TestStellarBurgersPasswordRecovery:
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery(self, login):
        recovery_page = PasswordRecoveryPage(login)
        recovery_page.click_password_recovery()
        name_button = WebDriverWait(login, 5).until(EC.visibility_of_element_located
                                                    (LoginLocators.BUTTON_LOGIN)).text
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
