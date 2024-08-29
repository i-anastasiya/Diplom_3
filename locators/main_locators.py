from selenium.webdriver.common.by import By


class MainLocators:

    # кнопка Личный Кабинет на главной
    PERSONAL_AREA_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")

    # Тег Булки на главной
    TAG_1 = (By.XPATH, ".//span[text()='Булки']")

    # Кнопка Лента заказов на главной сайта
    BUTTON_LIST_ORDER = By.XPATH, "//p[text()='Лента Заказов']"

    # Ингридиет для булочек
    INGREDIENT_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    # Заголовок Детали ингридиента в окне
    TITLE_WINDOW_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Название ингридиента в открытом окне
    INGREDIENT_NAME = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    # Крестик в окне
    BUTTON_CLOSE = By.XPATH, "//button[contains(@class, 'close')]"

    # Поле для добавления наших ингридиентов
    ADDING_INGERIDIENTS_FIELD = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"

    # Цена первой булочки
    INGREDIENT_PRICE_1 = By.XPATH, "BurgerIngredient_ingredient__price__3p5Rm-988"

    # Общая цена ингридиентов
    ALL_INGREDIENT_PRICE = By.XPATH, '//p[@class="text text_type_digits-medium mr-3"]'
