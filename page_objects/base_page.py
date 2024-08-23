import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем появление элемента")
    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидаем появление элемента и забираем у него текст")
    def wait_element_visibility_of_element_located_text(self, locator):
        text_locator = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text
        return text_locator

    @allure.step("Ожидаем появление элемента и забираем у него текст")
    def wait_and_click(self, locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located
                                                      (locator))
        element.click()

    @allure.step('Авторизация пользователя')
    def login_personal_account(self):
        self.driver.find_element(*LoginLocators.EMAIL).send_keys(Constants.EMAIL)
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(Constants.PASSWORD)
        element = self.driver.find_element(*LoginLocators.AUTH_BUTTON_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Тап на кнопку "Лента заказов"')
    def click_list_order(self):
        element = self.driver.find_element(*MainLocators.BUTTON_LIST_ORDER)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Тап на на кнопку "Конструктор"')
    def click_constructor(self):
        element = self.driver.find_element(*MainLocators.BUTTON_CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Тап на на кнопку "Личный кабинет"')
    def click_personal_account(self):
        element = self.driver.find_element(*MainLocators.PERSONAL_AREA_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Закрывает всплывающие окно с ингридиентами')
    def close_ingredient(self):
        element = self.driver.find_element(*MainLocators.BUTTON_CLOSE)
        self.driver.execute_script("arguments[0].click();", element)


