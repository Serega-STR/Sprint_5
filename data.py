import random
from selenium.webdriver.support.wait import WebDriverWait


class Credentials():
    EMAIL = 'aboleshev_38_39_fs@mail.ru'
    PASSWORD = '12345678'

class Generator():
    def create_password():
        password = f'{random.randint(100_000,999_999)}'
        return password

    def create_email():
        email = f'sergey_aboleshev_38_39_fs_{random.randint(100,999)}@mail.ru'
        return email

    def create_too_short_password():
        password = f'{random.randint(10_000,99_999)}'
        return password

class Wait():
    def wait(driver):
        # задаем время ожидания драйвера браузера - до 3 сек
        return WebDriverWait(driver, 3)
        
