import allure

from page_objects.main_page import MainPage
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
        name_button = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.TITLE_LIST_ORDER)
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
        recovery_page.click_ingredient()
        recovery_page.close_ingredient()
        assert driver.find_element(*MainLocators.INGREDIENT_1)

    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient(self, driver):
        recovery_page = MainPage(driver)
        # запоминаем общую цену до того как добавили ингридиент
        price_1 = recovery_page.wait_element_visibility_of_element_located_text(MainLocators.ALL_INGREDIENT_PRICE)
        price_value_1 = float(price_1.replace(',', '.'))
        recovery_page.add_ingredient()
        # запоминаем цену после того как добавили ингридиент
        price_2 = recovery_page.wait_element_visibility_of_element_located_text(MainLocators.ALL_INGREDIENT_PRICE)
        price_value_2 = float(price_2.replace(',', '.'))
        assert price_value_1 < price_value_2

    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_placing_an_order(self, login):
        recovery_page = OrdersPage(login)
        recovery_page.login_personal_account()
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page.tap_placing_an_order()
        title = recovery_page.wait_element_visibility_of_element_located_text(OrdersLocators.TITLE_ORDER_ID)
        assert title == 'идентификатор заказа'
