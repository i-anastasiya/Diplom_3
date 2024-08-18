import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture(scope="function", params=["Chrome", "Firefox"])
def driver(request):
    # фикстура инициализирует браузер и открывает его на нужной странице нашего сайта
    if request.param == "Chrome":
        browser = webdriver.Chrome()
    elif request.param == "Firefox":
        browser = webdriver.Firefox()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def list_order(driver):
    # фикстура для открытия экрана со списками заказов
    driver.get(Constants.URL_LIST_ORDER)
    return driver

@pytest.fixture
def login(driver):
    # фикстура для открытия экрана авторизации
    driver.get(Constants.URL_LOGIN)
    return driver
