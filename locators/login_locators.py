from selenium.webdriver.common.by import By


class LoginLocators:
    # Кнопка восстановить пароль на экране авторизации
    BUTTON_RECOVERY = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')

    # Кнопка Войти на экране Восстановления пароля и на экране регистрации
    BUTTON_LOGIN = (By.XPATH, ".//a[text()='Войти']")

    # поле ввода email на экране восстановления пароля
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")

    # кнопка Восстановить на экране востановления пароля
    BTN_RECOVERY = (By.XPATH, "//button[text()='Восстановить']")

    # заголовок Восстановление пароля
    TITLE_RECOVERY = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # поле ввода пароля на экране авторизации
    INPUT_PASSWORD = (By.XPATH, './/form/fieldset[2]/div/div/input')

    # иклонка глаза в инпуте пароля
    ICON_EYE = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")

    # активное поле пароля, после тапа на иконку глаза
    INPUT_PASSWORD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")

    # поле ввода email на экране авторизации
    EMAIL = (By.XPATH, './/form/fieldset[1]/div/div/input')

    # поле ввода пароля на экране авторизации
    PASSWORD = (By.XPATH, './/form/fieldset[2]/div/div/input')

    # кнопка Войти в аккаунт на экране авторизации
    AUTH_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Войти']")

    # Кнопка Зарегистрироваться на экране авторизации
    REGISTRATION_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # Кнопка Выход в личном кабинете
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")
