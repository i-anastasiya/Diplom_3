import allure

from locators.list_order_locators import ListOrderLocators


class ListOrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие заказа, который в работе')
    def tap_order_list(self):
        element = self.driver.find_element(*ListOrderLocators.LIST_ORDER_1)
        self.driver.execute_script("arguments[0].click();", element)
