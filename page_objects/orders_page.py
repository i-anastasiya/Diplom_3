import allure
from page_objects.base_page import BasePage
from locators.order_locators import OrdersLocators

class OrdersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Тап на кнопку Оформить заказ')
    def tap_placing_an_order(self):
        element = self.driver.find_element(*OrdersLocators.COME_IN_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
