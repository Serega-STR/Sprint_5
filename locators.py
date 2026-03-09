from selenium.webdriver.common.by import By

class Locators():
    HREF_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]') #  элемент навигационной панели личный кабинет 
    HREF_REGISTER = (By.CSS_SELECTOR, 'a[href="/register"]') # ссылка зарегистрироваться
    BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка зарегистрироваться
    REGISTER_NAME_FIELD = (By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input') # поля ввода имени  (форма регистрации)
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input') # поля ввода емейл (форма регистрации) 
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]') # поля ввода пароля (форма регистрации)
    LOG_IN_BUTTON = (By.XPATH, '//div[@class="Auth_login__3hAey"]/form/button[text()="Войти"]') # кнопка войти в ЛК
    PLACE_AN_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # кнопка оформить заказ
    MESSAGE_WRONG_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]') # сообщение о неправильном пароле
    LOG_IN_BUTTON_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка входа в аккаунт на главной странице
    LOG_IN_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//a[@href="/login"]') # кнопка входа в аккаунт на странице регистрации
    HREF_RECOVER_PASSWORD = (By.CSS_SELECTOR, 'a[href="/forgot-password"]') # ссылка на восстановление пароля
    LOG_IN_BUTTON_RECOVER_PASSWORD = (By.XPATH, '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]') # кнопка входа в аккаунт в меню восстановления пароля
    HREF_CONSTRUCTOR = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/"]') #  элемент навигационной панели конструктор 
    HREF_LOGO = (By.CSS_SELECTOR, 'div > a[href="/"]') #  элемент навигационной панели логотип
    LOG_OUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button") and text()="Выход"]') # кнопка выхода из аккаунта

    BUTTON_BREAD = (By.XPATH, '//span[text()="Булки"]/parent::*')  # кнопка конструктора 'Булки'
    BUTTON_SAUCES = (By.XPATH, '//span[text()="Соусы"]/parent::*')  # кнопка конструктора 'Соусы'
    BUTTON_TOPPINGS = (By.XPATH, '//span[text()="Начинки"]/parent::*')  # кнопка конструктора 'начинки'

    SCROLL_BREAD = (By.XPATH, '//h2[text()="Булки"]') # раздел скролла Булки
    SCROLL_SAUCES = (By.XPATH, '//h2[text()="Соусы"]') # раздел скролла Соусы
    SCROLL_TOPPINGS = (By.XPATH, '//h2[text()="Начинки"]') # раздел скролла начинки

