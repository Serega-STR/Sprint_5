import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Credentials


class TestLogin:
    def test_login_via_the_button_in_the_password_recovery_form_success(self, driver, wait):

        """
            Тест: вход в аккаунт через форму восстановления пароля
        """     

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
        wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

        # сравниваем ожидаемую и текущую страницу после авторизации
        
        assert driver.current_url == main_site

        # вместо кнопки "Войти в аккаунт" отображается кнопка "Оформить заказ"

        assert driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

        #pytest tests/test_login_via_the_button_in_the_password_recovery_form_success.py -v #ПЕРЕД СДАЧЕЙ УДАЛИТЬ