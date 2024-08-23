import allure
from locators.main_locators import MainLocators
from selenium.webdriver import ActionChains


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбирает ингридиент')
    def click_ingredient(self):
        element = self.driver.find_element(*MainLocators.INGREDIENT_1)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(*MainLocators.TITLE_WINDOW_INGREDIENT)


    @allure.step('Добавляет ингридиент в заказ')
    def add_ingredient(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*MainLocators.INGREDIENT_1)
        element_1 = self.driver.find_element(*MainLocators.ADDING_INGERIDIENTS_FIELD)
        actions.drag_and_drop(element, element_1).perform()
