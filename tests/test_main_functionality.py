import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.orders_page import OrdersPage
from locators.main_locators import MainLocators
from locators.list_order_locators import ListOrderLocators
from locators.order_locators import OrdersLocators


class TestStellarBurgersMainFunctionaly:
    @allure.description('Переход по клику на «Конструктор»')
    def test_go_constructor(self, login):
        recovery_page = MainPage(login)
        recovery_page.click_constructor()
        assert login.find_element(*MainLocators.TAG_1).text == 'Булки'

    @allure.description('Переход по клику на «Лента заказов»')
    def test_go_list_order(self, driver):
        recovery_page = MainPage(driver)
        recovery_page.click_list_order()
        name_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                    ((ListOrderLocators.TITLE_LIST_ORDER))).text
        assert name_button == 'Лента заказов'

    @allure.description('Клик на ингредиент, появится всплывающее окно с деталями,')
    def test_open_ingredient(self, driver):
        recovery_page = MainPage(driver)
        name = driver.find_element(*MainLocators.INGREDIENT_1).text
        recovery_page.click_ingredient()
        assert driver.find_element(*MainLocators.INGREDIENT_NAME).text == name

    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient(self, driver):
        recovery_page = MainPage(driver)
        name = driver.find_element(*MainLocators.INGREDIENT_1).text
        recovery_page.click_ingredient()
        # проверяем, что точно отрылось окно
        assert driver.find_element(*MainLocators.INGREDIENT_NAME).text == name
        recovery_page.close_ingredient()
        assert driver.find_element(*MainLocators.INGREDIENT_1)

    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient(self, driver):
        recovery_page = MainPage(driver)
        # запоминаем общую цену до того как добавили ингридиент
        price_1 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                       ((MainLocators.ALL_INGREDIENT_PRICE))).text
        price_value_1 = float(price_1.replace(',', '.'))
        recovery_page.add_ingredient()
        # запоминаем цену после того как добавили ингридиент
        price_2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                                     ((MainLocators.ALL_INGREDIENT_PRICE))).text
        price_value_2 = float(price_2.replace(',', '.'))
        assert price_value_1 < price_value_2

    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_placing_an_order(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_1.tap_placing_an_order()
        title = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.TITLE_ORDER_ID))).text
        assert title == 'идентификатор заказа'
