from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from driver_helper import DriverHelper
from helper import Helper
from locators import Locators


class TestRegistration:


    def test_register_new_user(self, driver):
        wb = DriverHelper(driver)
        driver.get(Data.REGISTER_URL)
        name_input = wb.wait_get_element(Locators.PROFILE_NAME_INPUT)
        email_input = wb.wait_get_element(Locators.REGISTER_EMAIL_INPUT)
        password_input = driver.find_element(*Locators.REGISTER_PASSWORD_INPUT)
        name_input.send_keys(Data.NAME)
        email = Helper.get_email()
        password = Helper.get_password()
        email_input.send_keys(email)
        password_input.send_keys(password)
        driver.find_element(*Locators.REGISTER_REGISTER_BUTTON).click()
        login_button = wb.wait_get_element(Locators.LOGIN_BUTTON)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        login_button.click()
        wb.wait_get_element(Locators.FOOD_ITEMS)
        items = driver.find_elements(*Locators.FOOD_ITEMS)
        assert len(items) > 1
        assert items[0].is_displayed() == True


    def test_enter_wrong_password(self, driver):
        wb = DriverHelper(driver)
        driver.get(Data.REGISTER_URL)
        name_input = wb.wait_get_element(Locators.PROFILE_NAME_INPUT)
        email_input = wb.wait_get_element(Locators.REGISTER_EMAIL_INPUT)
        password_input = driver.find_element(*Locators.REGISTER_PASSWORD_INPUT)
        name_input.send_keys(Data.NAME)
        email = Helper.get_email()
        email_input.send_keys(email)
        password_input.send_keys("Pass2")
        driver.find_element(*Locators.REGISTER_REGISTER_BUTTON).click()
        error_hint = wb.wait_get_element(Locators.PASSWORD_ERROR_HINT)
        assert error_hint.text == "Некорректный пароль"

