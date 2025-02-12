from time import sleep

import pytest

from asserts import PageAsserts
from conftest import driver
from data import Data
from driver_helper import DriverHelper
from locators import Locators


class TestLoginPage:

    def test_login_successfully(self, driver_in):
        items = driver_in.find_elements(*Locators.FOOD_ITEMS)
        assert len(items) > 1

    def test_login_incorrect_password(self, driver):
        wb = DriverHelper(driver)
        driver.get(Data.SITE_LOGIN_URL)
        password = driver.find_element(*Locators.PASSWORD_INPUT)
        password.send_keys("BadPs")
        email = wb.wait_get_element(Locators.EMAIL_INPUT)
        email.send_keys(Data.EMAIL)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        error_hint = wb.wait_get_element(Locators.PASSWORD_ERROR_HINT)
        assert error_hint.text == "Некорректный пароль"

    def test_login_page_opened_if_click_profile_link(self, driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.TOP_MENU_PROFILE_LINK).click()
        PageAsserts.assert_login_page_loaded(driver)

    def test_login_page_opened_if_click_enter_button(self, driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.ENTER_BUTTON).click()
        PageAsserts.assert_login_page_loaded(driver)

    def test_login_page_opened_if_click_from_forgot_password_page(self, driver):
        wb = DriverHelper(driver)
        driver.get(Data.FORGOT_PASS_URL)
        wb.wait_get_element(Locators.LOGIN_LINK).click()
        PageAsserts.assert_login_page_loaded(driver)

    def test_login_page_opened_if_click_from_register_page(self, driver):
        wb = DriverHelper(driver)
        driver.get(Data.REGISTER_URL)
        wb.wait_get_element(Locators.LOGIN_LINK).click()
        PageAsserts.assert_login_page_loaded(driver)

