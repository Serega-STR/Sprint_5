import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators

import random
import time #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

class TestTransition:
    def test_personal_account_to_constructor(self, driver_pers_acc_page, wait_pap):

        """
            Тест: переход из ЛК в конструктор 
        """
        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ
        """
        # драйвер загружает ЛК
        driver.get(pers_acc_page)

         #выпонить вход в личный кабинет
        driver.find_element(*Locators.HREF_ACCOUNT).click()

        """

        # жмем кнопку "конструктор"
        driver_pers_acc_page.find_element(*Locators.HREF_CONSTRUCTOR).click()

        #сравниваем ожидаемую и текущую страницу после авторизации

        assert driver_pers_acc_page.current_url == main_site

        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

        #pytest tests/test_personal_account_to_constructor.py -v
