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
    def test_registration_too_short_password_error_message(self, driver, wait):

        """
            Тест: нельзя зарегистрироваться с паролем меньше 6 символов
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
        email = f'sergey_aboleshev_38_39_fs_{random.randint(100,999)}@mail.ru'
        email_field = driver.find_element(*Locators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        
        #заполняем поле пароль
        password = f'{random.randint(10_000,99_999)}'
        password_field = driver.find_element(*Locators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)

        
        #жмем кнопку регистрации
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        # ждем появления сообщения "Некорректный пароль"
        element = wait.until(EC.visibility_of_element_located(Locators.MESSAGE_WRONG_PASSWORD))
        
        # проверяем, что текст элемента соответствует ожидаемому
        assert element.text == 'Некорректный пароль'
        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

        #pytest tests/test_registration_too_short_password_error_message.py -v