import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
from page_objects.list_order_page import ListOrderPage
from page_objects.login_page import LoginPage
from locators.list_order_locators import ListOrderLocators
from locators.order_locators import OrdersLocators
from page_objects.orders_page import OrdersPage


class TestStellarBurgersOrderList:
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details(self, list_order):
        recovery_page = ListOrderPage(list_order)
        name_button = WebDriverWait(list_order, 3).until(EC.visibility_of_element_located
                                                     ((ListOrderLocators.TITLE_LIST_ORDER))).text
        assert name_button == 'Лента заказов'
        recovery_page.tap_order_list()
        WebDriverWait(list_order, 3).until(EC.visibility_of_element_located
                                           ((ListOrderLocators.WINDOW_ORDER)))
        assert list_order.find_element(*ListOrderLocators.WINDOW_ORDER)

    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_details(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page_2 = MainPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_2.click_list_order()
        all_orders = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((ListOrderLocators.ALL_ORDERS))).text
        recovery_page_2.click_constructor()
        recovery_page_1.tap_placing_an_order()
        recovery_page_2.close_ingredient()
        recovery_page_2.click_list_order()
        time.sleep(10)
        all_orders_1 = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                   ((ListOrderLocators.ALL_ORDERS))).text
        assert all_orders < all_orders_1

    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_details_today(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page_2 = MainPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_2.click_list_order()
        all_orders_today = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                   ((ListOrderLocators.ALL_ORDER_TODAY))).text
        recovery_page_2.click_constructor()
        recovery_page_1.tap_placing_an_order()
        recovery_page_2.close_ingredient()
        recovery_page_2.click_list_order()
        time.sleep(10)
        all_orders_today_1 = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                     ((ListOrderLocators.ALL_ORDER_TODAY))).text
        assert all_orders_today < all_orders_today_1

    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_order_numder(self, login):
        recovery_page = LoginPage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page_2 = MainPage(login)
        recovery_page.login_personal_account()
        # проверяем, что мы действительно авторизовались
        name_button = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                    ((OrdersLocators.COME_IN_BUTTON))).text
        assert name_button == 'Оформить заказ'
        recovery_page_1.tap_placing_an_order()
        recovery_page_2.close_ingredient()
        recovery_page_2.click_list_order()
        time.sleep(10)
        numder_my_order = WebDriverWait(login, 3).until(EC.visibility_of_element_located
                                                           ((ListOrderLocators.ORDER_NUMBER))).text
        numder_orders = WebDriverWait(login, 10).until(EC.visibility_of_element_located
                                                        ((ListOrderLocators.MY_ORDER_NUMBER))).text
        assert numder_my_order in numder_orders
