import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials


class TestLogin:
    def test_login_via_the_button_in_the_registration_form_success(self, driver, wait):

        """
            Тест: вход в аккаунт через форму регистрации
        """     

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
        wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site

        # вместо кнопки "Войти в аккаунт" отображается кнопка "Оформить заказ"

        assert driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'