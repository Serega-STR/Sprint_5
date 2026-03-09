import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators 

import random
import time #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

class TestRegistration:
    @staticmethod
    def create_password():
        password = f'{random.randint(100_000,999_999)}'
        return password

    @staticmethod
    def create_email():
        email = f'sergey_aboleshev_38_39_fs_{random.randint(100,999)}@mail.ru'
        return email

    def test_succesful_registration_can_log_in(self, driver, wait):

        """
            Тест: после регистрации пользователь может войти с теми же кредами
        """     

        #выпонить вход в личный кабинет
        driver.find_element(*Locators.HREF_ACCOUNT).click()

        #ждем загрузки страницы ЛК  
        wait.until(EC.element_to_be_clickable(Locators.HREF_REGISTER))

        #переход в раздел регистрации
        driver.find_element(*Locators.HREF_REGISTER).click()

        #ждем загрузки страницы регистрации
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_REGISTRATION))

        #заполняем поле имя
        name_field = driver.find_element(*Locators.REGISTER_NAME_FIELD)
        name_field.send_keys('Вася')

        #заполняем поле email
        email = TestRegistration.create_email()
        email_field = driver.find_element(*Locators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        
        #заполняем поле пароль
        password = TestRegistration.create_password()
        password_field = driver.find_element(*Locators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)

        #жмем кнопку регистрации
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        #ждем загрузки страницы ЛК
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        #пробуем войти в ЛК с вновь зарегистрированными кредами
        pers_acc_email = driver.find_element(*Locators.REGISTER_NAME_FIELD)
        pers_acc_email.send_keys(email)
        pers_acc_password = driver.find_element(*Locators.REGISTER_EMAIL_FIELD)
        pers_acc_password.send_keys(password)

        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        #сравниваем ожидаемую и текущую страницу после авторизации
        
        #print(f' Страница после авторизации: {driver.current_url}')  #ПЕРЕД СДАЧЕЙ УДАЛИТЬ
        assert driver.current_url == main_site 

        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

       
        #pytest tests/test_successful_registration.py -v
        #pytest tests/ -v
