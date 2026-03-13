import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials


class TestLogout:
    def test_personal_account_logout(self, driver_pers_acc_page, wait_pap):
        
        """
            Тест: выход из ЛК
        """
        # вход в ЛК с имеющимися валидными кредами
        driver_pers_acc_page.find_element(*Locators.REGISTER_NAME_FIELD).send_keys(Credentials.EMAIL)
        driver_pers_acc_page.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver_pers_acc_page.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        wait_pap.until(EC.element_to_be_clickable(Locators.HREF_ACCOUNT))

        # жмем на кнопку ЛК 
        driver_pers_acc_page.find_element(*Locators.HREF_ACCOUNT).click()

        # ждем загрузки страницы личного профиля
        wait_pap.until(EC.element_to_be_clickable(Locators.LOG_OUT_BUTTON))

        # жмем на кнопку "выход" 
        driver_pers_acc_page.find_element(*Locators.LOG_OUT_BUTTON).click()

        # ждем загрузки страницы (смена URL)

        wait_pap.until(EC.url_to_be(pers_acc_page))

        # сравниваем ожидаемую и текущую страницу после выхода
        assert driver_pers_acc_page.current_url == pers_acc_page