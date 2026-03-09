import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials

import random
import time #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

class TestLogin:
    def test_firefox_main_page_login_success(self, driver_ff, wait_ff):

        """
            Тест: вход по кнопке «Войти в аккаунт» на главной странице
        """     
        # ждем загрузки главной страницы
        wait_ff.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON_MAIN_PAGE))

        # нажать кнопку «Войти в аккаунт» на главной странице
        driver_ff.find_element(*Locators.LOG_IN_BUTTON_MAIN_PAGE).click()

        # ждем загрузки страницы ЛК
        wait_ff.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        # пробуем войти в ЛК с имеющимися валидными кредами
        pers_acc_email = driver_ff.find_element(*Locators.REGISTER_NAME_FIELD)
        pers_acc_email.send_keys(Credentials.EMAIL)
        driver_ff.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver_ff.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        wait_ff.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver_ff.current_url == main_site

        # вместо кнопки "Войти в аккаунт" отображается кнопка "Оформить заказ"

        assert driver_ff.find_element(*Locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

        #pytest tests/test_firefox_main_page_login_success.py -v #ПЕРЕД СДАЧЕЙ УДАЛИТЬ