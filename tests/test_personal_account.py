import allure
from locators.login_locators import LoginLocators
from page_objects.base_page import BasePage
from locators.order_locators import OrdersLocators

class TestStellarBurgersPersonalAccount:
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_open_personal_account(self, driver):
        recovery_page = BasePage(driver)
        recovery_page.click_personal_account()
        assert driver.find_element(*LoginLocators.INPUT_PASSWORD)

    @allure.description('Переход в раздел «История заказов»')
    def test_open_history_orders(self, login):
        recovery_page = BasePage(login)
        recovery_page.login_personal_account()
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page.click_personal_account()
        recovery_page.wait_and_click(OrdersLocators.BTN_HISTORY_ORDERS)
        assert login.find_element(*OrdersLocators.BTN_HISTORY_ORDERS)

    @allure.description('Выход из аккаунт')
    def test_logout(self, login):
        recovery_page = BasePage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page.click_personal_account()
        recovery_page.wait_and_click(LoginLocators.BUTTON_EXIT)
        title = recovery_page.wait_element_visibility_of_element_located_text(LoginLocators.REGISTRATION_BUTTON)
        assert title == 'Зарегистрироваться'
