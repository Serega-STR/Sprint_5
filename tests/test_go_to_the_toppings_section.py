import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators


class TestConstrutor:
    def test_go_to_the_toppings_section(self, driver, wait):
        
        """
            Тест: переход к разделу конструктора Булки
        """  

        # Ждём, пока элемент скролл-меню "начинки" станет видимым
        element = driver.find_element(*Locators.SCROLL_TOPPINGS)
        wait.until(EC.visibility_of(element))

        # Прокручиваем к элементу
        driver.execute_script("arguments[0].scrollIntoView();", element)
        
        # проверяем видимость 
        assert element.is_displayed(), "Элемент не отображается"
