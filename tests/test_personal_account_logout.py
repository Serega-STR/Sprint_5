import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials, Wait


class TestLogout:
    def test_personal_account_logout(self, driver):
        
        """
            Тест: выход из ЛК
        """

        # открываем сайт с помощью драйвера
        driver.get(pers_acc_page)

        # задаем ожидание браузера
        wait = Wait.wait(driver)

        # вход в ЛК с имеющимися валидными кредами
        driver.find_element(*Locators.PERS_ACC_EMAIL_FIELD).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.PERS_ACC_PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        wait.until(EC.element_to_be_clickable(Locators.HREF_ACCOUNT))

        # жмем на кнопку ЛК 
        driver.find_element(*Locators.HREF_ACCOUNT).click()

        # ждем загрузки страницы личного профиля
        wait.until(EC.element_to_be_clickable(Locators.LOG_OUT_BUTTON))

        # жмем на кнопку "выход" 
        driver.find_element(*Locators.LOG_OUT_BUTTON).click()

        # ждем загрузки страницы (смена URL)

        wait.until(EC.url_to_be(pers_acc_page))

        # сравниваем ожидаемую и текущую страницу после выхода
        assert driver.current_url == pers_acc_page

        # кнопка ЛК войти
        assert driver.find_element(*Locators.LOG_IN_BUTTON)