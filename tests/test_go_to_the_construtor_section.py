import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators
from data import Wait


class TestConstrutor:
    

    def test_go_to_the_bread_section(self, driver):
        
        """
            Тест: переход к разделу конструктора Булки
        """

        # задаем ожидание браузера
        wait = Wait.wait(driver)

        # Ждём, пока элемент скролл-меню "начинки" станет видимым
        element = driver.find_element(*Locators.SCROLL_TOPPINGS)
        wait.until(EC.visibility_of(element))

        # Прокручиваем к сначала элементу  "начинки"
        driver.execute_script("arguments[0].scrollIntoView();", element)

        # жмем кнопку конструктора "булки"
        element = driver.find_element(*Locators.BUTTON_BREAD)
        element.click()
        class_value = element.get_attribute('class')
        
        # проверяем что поменялся класс элемента
        assert 'current' in class_value

    def test_go_to_the_sauces_section(self, driver):
        
        """
            Тест: переход к разделу конструктора Соусы
        """  

        # задаем ожидание браузера
        wait = Wait.wait(driver)

        # Ждём, пока элемент скролл-меню "соусы" станет видимым
        element = driver.find_element(*Locators.SCROLL_SAUCES)
        wait.until(EC.visibility_of(element))

        # жмем кнопку конструктора "соусы"
        element = driver.find_element(*Locators.BUTTON_SAUCES)
        element.click()
        class_value = element.get_attribute('class')
        
        # проверяем что поменялся класс элемента
        assert 'current' in class_value

    def test_go_to_the_toppings_section(self, driver):
        
        """
            Тест: переход к разделу конструктора Начинки
        """  

        # задаем ожидание браузера
        wait = Wait.wait(driver)

        # Ждём, пока элемент скролл-меню "начинки" станет видимым
        element = driver.find_element(*Locators.SCROLL_TOPPINGS)
        wait.until(EC.visibility_of(element))

        # жмем кнопку конструктора "начинки"
        element = driver.find_element(*Locators.BUTTON_TOPPINGS)
        element.click()
        class_value = element.get_attribute('class')
        
        # проверяем что поменялся класс элемента
        assert 'current' in class_value
