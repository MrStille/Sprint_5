import pytest
from selenium import webdriver

from data import Data
from driver_helper import DriverHelper
from locators import Locators


@pytest.fixture(scope='function')
def driver_init():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver(driver_init):
    driver_init.get(Data.SITE_URL)
    yield driver_init

@pytest.fixture(scope='function')
def driver_in(driver_init):
    wb = DriverHelper(driver_init)
    driver_init.get(Data.SITE_LOGIN_URL)
    email = wb.wait_get_element(Locators.EMAIL_INPUT)
    email.send_keys(Data.EMAIL)
    password = driver_init.find_element(*Locators.PASSWORD_INPUT)
    password.send_keys(Data.PASSWORD)
    driver_init.find_element(*Locators.LOGIN_BUTTON).click()
    wb.wait_get_element(Locators.FOOD_ITEMS)
    yield driver_init