import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials, Wait


class TestLogin:
    def test_main_page_login_success(self, driver):

        """
            Тест: вход по кнопке «Войти в аккаунт» на главной странице
        """     

        # задаем ожидание
        wait = Wait.wait(driver)

        # нажать кнопку «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOG_IN_BUTTON_MAIN_PAGE).click()

        # ждем загрузки страницы ЛК
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        # пробуем войти в ЛК с имеющимися валидными кредами
        pers_acc_email = driver.find_element(*Locators.REGISTER_NAME_FIELD)
        pers_acc_email.send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        assert wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site
        

    def test_main_page_personal_account_login_success(self, driver):
        
        """
            Тест: вход в аккаунт через ЛК
        """   

        # задаем ожидание
        wait = Wait.wait(driver)

        # нажать кнопку «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOG_IN_BUTTON_MAIN_PAGE).click()

        # ждем загрузки страницы ЛК
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        # пробуем войти в ЛК с имеющимися валидными кредами
        pers_acc_email = driver.find_element(*Locators.REGISTER_NAME_FIELD)
        pers_acc_email.send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        assert wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site
        

    def test_login_via_the_button_in_the_registration_form_success(self, driver):

        """
            Тест: вход в аккаунт через форму регистрации
        """  
   
        # задаем ожидание
        wait = Wait.wait(driver)

        # нажать кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.HREF_ACCOUNT).click()

        #ждем загрузки страницы ЛК  
        wait.until(EC.element_to_be_clickable(Locators.HREF_REGISTER))

        #переход в раздел регистрации
        driver.find_element(*Locators.HREF_REGISTER).click()

        #ждем загрузки страницы регистрации
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON_REGISTRATION_PAGE))

        # ЖМЕМ ссылку "Войти"
        driver.find_element(*Locators.LOG_IN_BUTTON_REGISTRATION_PAGE).click()

        # ждем загрузки страницы ЛК  
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        # пробуем войти в ЛК с имеющимися валидными кредами
        pers_acc_email = driver.find_element(*Locators.REGISTER_NAME_FIELD)
        pers_acc_email.send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        assert wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site


    def test_login_via_the_button_in_the_password_recovery_form_success(self, driver):

        """
            Тест: вход в аккаунт через форму восстановления пароля
        """     

        # задаем ожидание
        wait = Wait.wait(driver)

        # нажать кнопку «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOG_IN_BUTTON_MAIN_PAGE).click()

        # ждем загрузки страницы ЛК
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON))

        # жмем ссылку "Восстановить пароль"
        driver.find_element(*Locators.HREF_RECOVER_PASSWORD).click()

        # ждем загрузки страницы восстановления пароля
        wait.until(EC.element_to_be_clickable(Locators.LOG_IN_BUTTON_RECOVER_PASSWORD))

        #  жмем кнопку "войти" в разделе "вспомнили пароль?"
        driver.find_element(*Locators.LOG_IN_BUTTON_RECOVER_PASSWORD).click()

        # пробуем войти в ЛК с имеющимися валидными кредами
        driver.find_element(*Locators.REGISTER_NAME_FIELD).send_keys(Credentials.EMAIL)
        driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()

        # ждем загрузки главной страницы
        assert wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site

    