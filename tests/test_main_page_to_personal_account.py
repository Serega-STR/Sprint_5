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
    def test_main_page_to_personal_account(self, driver, wait):

        """
            Тест: переход с главной страницы по клику в ЛК
        """     

        #выпонить вход в личный кабинет
        driver.find_element(*Locators.HREF_ACCOUNT).click()

        #ждем загрузки страницы ЛК  
        wait.until(EC.element_to_be_clickable(Locators.HREF_REGISTER))

        

        #сравниваем ожидаемую и текущую страницу после авторизации
        
        #print(f' Страница после авторизации: {driver.current_url}')  #ПЕРЕД СДАЧЕЙ УДАЛИТЬ
        assert driver.current_url == pers_acc_page 

        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

        #pytest tests/test_main_page_to_personal_account.py -v