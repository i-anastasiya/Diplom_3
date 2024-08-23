import allure
import time
from page_objects.list_order_page import ListOrderPage
from page_objects.base_page import BasePage
from locators.list_order_locators import ListOrderLocators
from locators.order_locators import OrdersLocators
from page_objects.orders_page import OrdersPage


class TestStellarBurgersOrderList:
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details(self, list_order):
        recovery_page = ListOrderPage(list_order)
        recovery_page_1 = BasePage(list_order)
        recovery_page_1.wait_element_visibility_of_element_located(ListOrderLocators.TITLE_LIST_ORDER)
        recovery_page.tap_order_list()
        recovery_page_1.wait_element_visibility_of_element_located(ListOrderLocators.WINDOW_ORDER)
        assert list_order.find_element(*ListOrderLocators.WINDOW_ORDER)

    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_details(self, login):
        recovery_page = BasePage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page.login_personal_account()
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page.click_list_order()
        all_orders = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.ALL_ORDERS)
        recovery_page.click_constructor()
        recovery_page_1.tap_placing_an_order()
        recovery_page.close_ingredient()
        recovery_page.click_list_order()
        time.sleep(10)
        all_orders_1 = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.ALL_ORDERS)
        assert all_orders < all_orders_1

    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_details_today(self, login):
        recovery_page = BasePage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page.login_personal_account()
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page.click_list_order()
        all_orders_today = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.ALL_ORDER_TODAY)
        recovery_page.click_constructor()
        recovery_page_1.tap_placing_an_order()
        recovery_page.close_ingredient()
        recovery_page.click_list_order()
        time.sleep(10)
        all_orders_today_1 = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.ALL_ORDER_TODAY)
        assert all_orders_today < all_orders_today_1

    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_order_numder(self, login):
        recovery_page = BasePage(login)
        recovery_page_1 = OrdersPage(login)
        recovery_page.login_personal_account()
        recovery_page.wait_element_visibility_of_element_located(OrdersLocators.COME_IN_BUTTON)
        recovery_page_1.tap_placing_an_order()
        recovery_page.close_ingredient()
        recovery_page.click_list_order()
        time.sleep(10)
        numder_my_order = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.ORDER_NUMBER)
        numder_orders = recovery_page.wait_element_visibility_of_element_located_text(ListOrderLocators.MY_ORDER_NUMBER)
        assert numder_my_order in numder_orders
