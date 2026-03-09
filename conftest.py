import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from urls import *

# ФИКСТУРЫ ДЛЯ БРАУЗЕРА CHROME

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless") # запуск без явного отображения браузера на экране

    # создаем драйвер для браузера (Google Chrome) с вышеуказанными опциями
    driver = webdriver.Chrome(options=options)
    
    # открываем сайт с помощью драйвера
    driver.get(main_site)

    # приостанавливаем этот код, передаем драйвер в тест
    yield driver

    # после выполнения теста закрываем браузер, останавливаем драйвер
    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    # задаем время ожидания драйвера браузера - до 3 сек
    return WebDriverWait(driver, 3)

@pytest.fixture(scope="function")
def driver_pers_acc_page():
    
    # создаем драйвер для браузера (Google Chrome)
    driver = webdriver.Chrome()

    # открываем сайт с помощью драйвера
    driver.get(pers_acc_page)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def wait_pap(driver_pers_acc_page):
    # задаем время ожидания драйвера браузера - до 3 сек
    return WebDriverWait(driver_pers_acc_page, 3)

# ФИКСТУРЫ ДЛЯ БРАУЗЕРА FIREFOX

@pytest.fixture(scope="function")
def driver_ff():
    
    # создаем драйвер для браузера (Firefox)
    driver = webdriver.Firefox()

    # пробуем открыть сайт с помощью драйвера
    
    try:
        # Открываем сайт
        driver.get(main_site)
        yield driver
    finally:
        # Гарантированно закрываем драйвер даже при ошибке
        driver.quit()

@pytest.fixture(scope="function")
def wait_ff(driver_ff):
    # задаем время ожидания драйвера браузера - до 5 сек
    return WebDriverWait(driver_ff, 5)
