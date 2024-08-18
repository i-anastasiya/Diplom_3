import allure
from locators.main_locators import MainLocators
from selenium.webdriver import ActionChains


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Тап на на кнопку "Личный кабинет"')
    def click_personal_account(self):
        element = self.driver.find_element(*MainLocators.PERSONAL_AREA_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Тап на на кнопку "Конструктор"')
    def click_constructor(self):
        element = self.driver.find_element(*MainLocators.BUTTON_CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Тап на кнопку "Лента заказов"')
    def click_list_order(self):
        element = self.driver.find_element(*MainLocators.BUTTON_LIST_ORDER)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Выбирает ингридиент')
    def click_ingredient(self):
        element = self.driver.find_element(*MainLocators.INGREDIENT_1)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(*MainLocators.TITLE_WINDOW_INGREDIENT)

    @allure.step('Закрывает всплывающие окно с ингридиентами')
    def close_ingredient(self):
        element = self.driver.find_element(*MainLocators.BUTTON_CLOSE)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Добавляет ингридиент в заказ')
    def add_ingredient(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*MainLocators.INGREDIENT_1)
        element_1 = self.driver.find_element(*MainLocators.ADDING_INGERIDIENTS_FIELD)
        actions.drag_and_drop(element, element_1).perform()
