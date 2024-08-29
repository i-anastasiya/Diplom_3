from selenium.webdriver.common.by import By


class OrdersLocators:

    # кнопка Оформить заказ на главной
    COME_IN_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # кнопка История заказаов в ЛК
    BTN_HISTORY_ORDERS = (By.XPATH, "//a[contains(text(), 'История заказов')]")

    # Текст Индитификатор заказа в окне, после оформления самого заказа
    TITLE_ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']")
