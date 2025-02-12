from selenium.webdriver.common.by import By


class Locators:
    #Страница логина
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_FORM_LABEL = (By.XPATH, "//h2[text()='Вход']")
    LOGOUT_BUTTON = (By.XPATH,"//button[text()='Выход']")

    # Страница профайла
    PROFILE_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    PROFILE_EMAIL_INPUT = (By.XPATH, "//label[text()='Логин']/parent::div/input")

    #Страница регистрации
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div/input")
    REGISTER_PASSWORD_INPUT = PASSWORD_INPUT
    REGISTER_REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Общие локаторы для нескольких страниц
    PASSWORD_ERROR_HINT = (
    By.XPATH, PASSWORD_INPUT[1] + "/ancestor::div[@class='input__container']/p[starts-with(@class,'input__error')]")
    LOGIN_LINK = (By.XPATH,"//a[text()='Войти']")

    # Главная(конструктор заказа) страница
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    TOP_MENU_PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    TOP_MENU_CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    TOP_MENU_SITE_LOGO = (By.XPATH, "//div[starts-with(@class,'AppHeader_header__logo')]")
    MIDDLE_MENU_BUNS = (By.XPATH, "//section[starts-with(@class,'BurgerIngredients_ingredients')]//span[text()='Булки']")
    MIDDLE_MENU_SAUCES = (By.XPATH, "//section[starts-with(@class,'BurgerIngredients_ingredients')]//span[text()='Соусы']")
    MIDDLE_MENU_TOPPINGS = (By.XPATH, "//section[starts-with(@class,'BurgerIngredients_ingredients')]//span[text()='Начинки']")
    FOOD_ITEMS = (By.XPATH, "//a[starts-with(@class,'BurgerIngredient_ingredient')]")

