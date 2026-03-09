import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import Locators


import random
import time #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

class TestConstrutor:
    def test_go_to_the_bread_section(self, driver, wait):
        
        """
            Тест: переход к разделу конструктора Булки
        """  

        # Ждём, пока элемент скролл-меню "начинки" станет видимым
        element = driver.find_element(*Locators.SCROLL_BREAD)
        wait.until(EC.visibility_of(element))

        # Прокручиваем к элементу
        driver.execute_script("arguments[0].scrollIntoView();", element)
        
        # проверяем видимость 
        assert element.is_displayed(), "Элемент не отображается"
        time.sleep(1) #ПЕРЕД СДАЧЕЙ УДАЛИТЬ

        #pytest tests/test_go_to_the_bread_section.py -v #ПЕРЕД СДАЧЕЙ УДАЛИТЬ
