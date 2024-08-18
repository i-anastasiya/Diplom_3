import allure
from locators.login_locators import LoginLocators
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from locators.order_locators import OrdersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersPersonalAccount:
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_open_personal_account(self, driver):
        recovery_page = MainPage(driver)
        recovery_page.click_personal_account()
        assert driver.find_element(*LoginLocators.INPUT_PASSWORD)

    @allure.description('Переход в раздел «История заказов»')
    def test_open_history_orders(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = MainPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                   ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_1.click_personal_account()
        element = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                (OrdersLocators.BTN_HISTORY_ORDERS))
        element.click()
        assert login.find_element(*OrdersLocators.BTN_HISTORY_ORDERS)

    @allure.description('Выход из аккаунт')
    def test_logout(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = MainPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_1.click_personal_account()
        name_button_1 = WebDriverWait(login, 3).until(EC.element_to_be_clickable
                                                (LoginLocators.BUTTON_EXIT))
        name_button_1.click()
        title = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                             ((LoginLocators.REGISTRATION_BUTTON))).text
        assert title == 'Зарегистрироваться'
