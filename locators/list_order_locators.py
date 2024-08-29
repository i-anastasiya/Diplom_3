from selenium.webdriver.common.by import By


class ListOrderLocators:

    # заголовок Лента заказов, на эране всех заказов
    TITLE_LIST_ORDER = By.XPATH, "//h1[text()='Лента заказов']"

    # Заказ в ленте заказов
    LIST_ORDER_1 = (By.XPATH, "//div/ul/li[1]")

    # Окно заказа
    WINDOW_ORDER = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")

    # Каунтер всех заказов
    ALL_ORDERS = (By.XPATH, ".//div/div[2]/p[2]")

    # Каунтер всех заказов за сегодня
    ALL_ORDER_TODAY = (By.XPATH,"//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # номер заказа
    ORDER_NUMBER = (By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]')

    # номер заказа в разделе готовятся
    MY_ORDER_NUMBER = (By.XPATH, "//div[@class='some-class']/ul[2]/li")
